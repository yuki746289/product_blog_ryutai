from __future__ import annotations

import csv
import html
import json
import os
import posixpath
import re
import shutil
import struct
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path.cwd()
OUT = Path('/tmp/formula-image-inventory')
CANDIDATES = OUT / 'candidates'

IMAGE_EXTENSIONS = {'.gif', '.png', '.jpg', '.jpeg', '.webp', '.bmp'}
SKIP_DIRS = {'.git', '.github', '.rules', '.document', 'responsive_navigation_v1.1'}
EXTERNAL_PREFIXES = ('http://', 'https://', '//', 'data:', 'javascript:')

IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.I | re.S)
SRC_RE = re.compile(r'\bsrc\s*=\s*(["\'])(.*?)\1', re.I | re.S)
ALT_RE = re.compile(r'\balt\s*=\s*(["\'])(.*?)\1', re.I | re.S)
TAG_RE = re.compile(r'<[^>]+>', re.S)
SPACE_RE = re.compile(r'\s+')


def decode_html(data: bytes):
    for encoding in ('cp932', 'shift_jis', 'utf-8-sig', 'utf-8'):
        try:
            return data.decode(encoding), encoding
        except UnicodeDecodeError:
            pass
    return data.decode('cp932', errors='replace'), 'cp932-replace'


def clean_text(value: str) -> str:
    value = TAG_RE.sub(' ', value)
    value = html.unescape(value)
    value = SPACE_RE.sub(' ', value)
    return value.strip()


def normalize_local_src(html_path: Path, src: str):
    src = html.unescape(src.strip())
    src = src.split('#', 1)[0].split('?', 1)[0]
    if not src or src.lower().startswith(EXTERNAL_PREFIXES):
        return None
    src = src.replace('\\', '/')
    base = html_path.parent.as_posix()
    joined = posixpath.normpath(posixpath.join(base, src))
    while joined.startswith('../'):
        joined = joined[3:]
    return joined.lstrip('./')


def image_dimensions(path: Path):
    try:
        data = path.read_bytes()
        suffix = path.suffix.lower()
        if suffix == '.png' and len(data) >= 24 and data[:8] == b'\x89PNG\r\n\x1a\n':
            return struct.unpack('>II', data[16:24])
        if suffix == '.gif' and len(data) >= 10 and data[:6] in (b'GIF87a', b'GIF89a'):
            return struct.unpack('<HH', data[6:10])
        if suffix in ('.jpg', '.jpeg') and len(data) > 4 and data[:2] == b'\xff\xd8':
            index = 2
            while index + 9 < len(data):
                if data[index] != 0xFF:
                    index += 1
                    continue
                marker = data[index + 1]
                index += 2
                if marker in (0xD8, 0xD9):
                    continue
                if index + 2 > len(data):
                    break
                length = int.from_bytes(data[index:index + 2], 'big')
                if length < 2 or index + length > len(data):
                    break
                if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    if index + 7 <= len(data):
                        height = int.from_bytes(data[index + 3:index + 5], 'big')
                        width = int.from_bytes(data[index + 5:index + 7], 'big')
                        return width, height
                index += length
    except OSError:
        pass
    return None, None


def classify(ref):
    path = ref['resolved_path'].lower()
    width = ref.get('width')
    height = ref.get('height')
    context = ref.get('context', '')
    tag_context = ref.get('tag_context', '').lower()
    basename = Path(path).name.lower()

    score = 0
    reasons = []

    if '.files/' in path and re.fullmatch(r'image\d+\.(gif|png|jpg|jpeg)', basename):
        score += 2
        reasons.append('Office連番画像')
    if re.search(r'(formula|equation|eq[_-]?\d|math)', basename):
        score += 4
        reasons.append('数式系ファイル名')
    if 'class="im"' in tag_context or "class='im'" in tag_context:
        score += 1
        reasons.append('中央画像段落')
    if width and height:
        if height <= 100 and width <= 750:
            score += 2
            reasons.append('低い横長画像')
        elif height <= 150 and width >= max(120, int(height * 1.5)):
            score += 1
            reasons.append('横長画像')
        if height >= 220 and width >= 220:
            score -= 2
            reasons.append('大きな図の可能性')
    if re.search(r'(式|方程式|定義|ここで|したがって|より|となる|表す|変形|代入|微分|積分|行列|ベクトル)', context):
        score += 1
        reasons.append('数式周辺語')
    if re.search(r'(図|グラフ|メッシュ|要素図|模式図|概念図|形状|写真)', context):
        score -= 1
        reasons.append('図周辺語')

    if score >= 3:
        category = 'formula_candidate'
    elif score >= 1:
        category = 'review'
    else:
        category = 'figure_or_other'
    return category, score, '; '.join(reasons)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CANDIDATES.mkdir(parents=True, exist_ok=True)

    html_files = []
    for path in ROOT.rglob('*.html'):
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        html_files.append(path)

    references = []
    missing = []
    encodings = Counter()

    for html_path in sorted(html_files):
        relative_html = html_path.relative_to(ROOT)
        text, encoding = decode_html(html_path.read_bytes())
        encodings[encoding] += 1

        for match in IMG_TAG_RE.finditer(text):
            tag = match.group(0)
            src_match = SRC_RE.search(tag)
            if not src_match:
                continue
            src = src_match.group(2).strip()
            resolved = normalize_local_src(relative_html, src)
            if not resolved:
                continue
            suffix = Path(resolved).suffix.lower()
            if suffix not in IMAGE_EXTENSIONS:
                continue

            alt_match = ALT_RE.search(tag)
            alt = clean_text(alt_match.group(2)) if alt_match else ''
            start = max(0, match.start() - 240)
            end = min(len(text), match.end() + 240)
            context = clean_text(text[start:end])[:420]
            parent_start = max(0, match.start() - 120)
            tag_context = text[parent_start:match.end()]
            image_path = ROOT / resolved
            exists = image_path.is_file()
            width = height = None
            size = None
            if exists:
                size = image_path.stat().st_size
                width, height = image_dimensions(image_path)
            else:
                missing.append({'html': relative_html.as_posix(), 'src': src, 'resolved': resolved})

            row = {
                'html': relative_html.as_posix(),
                'src': src,
                'resolved_path': resolved,
                'exists': exists,
                'extension': suffix,
                'size_bytes': size,
                'width': width,
                'height': height,
                'alt': alt,
                'context': context,
                'tag_context': tag_context,
            }
            category, score, reasons = classify(row)
            row['category'] = category
            row['score'] = score
            row['reasons'] = reasons
            references.append(row)

    # Deduplicate referenced images while preserving all referring pages.
    by_image = defaultdict(list)
    for ref in references:
        by_image[ref['resolved_path']].append(ref)

    unique_rows = []
    for resolved_path, refs in sorted(by_image.items()):
        best = max(refs, key=lambda r: r['score'])
        row = dict(best)
        row['reference_count'] = len(refs)
        row['pages'] = ' | '.join(sorted({ref['html'] for ref in refs}))
        row['categories_seen'] = ' | '.join(sorted({ref['category'] for ref in refs}))
        unique_rows.append(row)

        if row['exists'] and row['category'] in ('formula_candidate', 'review'):
            source = ROOT / resolved_path
            destination = CANDIDATES / resolved_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(source, destination)
            except OSError:
                pass

    csv_fields = [
        'resolved_path', 'category', 'score', 'reasons', 'width', 'height', 'size_bytes',
        'reference_count', 'pages', 'alt', 'context', 'exists', 'extension'
    ]
    with (OUT / 'inventory.csv').open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(unique_rows)

    (OUT / 'inventory.json').write_text(
        json.dumps(unique_rows, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    (OUT / 'missing.json').write_text(
        json.dumps(missing, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    category_counts = Counter(row['category'] for row in unique_rows)
    referenced_by_dir = Counter(Path(row['pages'].split(' | ')[0]).parts[0] if row['pages'] else '(root)' for row in unique_rows)

    summary_lines = [
        '# 数式画像棚卸し（自動一次分類）',
        '',
        f'- HTMLファイル数: {len(html_files)}',
        f'- 画像参照総数: {len(references)}',
        f'- 参照画像ユニーク数: {len(unique_rows)}',
        f'- 存在しないローカル画像参照: {len(missing)}',
        f'- formula_candidate: {category_counts["formula_candidate"]}',
        f'- review: {category_counts["review"]}',
        f'- figure_or_other: {category_counts["figure_or_other"]}',
        '',
        '## HTML文字コード',
        '',
    ]
    for name, count in encodings.most_common():
        summary_lines.append(f'- {name}: {count}')
    summary_lines += ['', '## 参照画像数（代表ページの第1階層別）', '']
    for name, count in referenced_by_dir.most_common():
        summary_lines.append(f'- {name}: {count}')
    summary_lines += [
        '',
        '## 注意',
        '',
        '- この分類はファイル名・画像寸法・周辺文脈による一次判定であり、数式内容の確定ではない。',
        '- `formula_candidate` と `review` の実画像を次工程で目視確認する。',
        '- 図・グラフ・メッシュ図は原則として画像を維持する。',
    ]
    (OUT / 'summary.md').write_text('\n'.join(summary_lines) + '\n', encoding='utf-8')

    print('\n'.join(summary_lines))
    print('Top formula candidates:')
    for row in sorted(unique_rows, key=lambda r: (-r['score'], r['resolved_path']))[:40]:
        if row['category'] == 'formula_candidate':
            print(f"  score={row['score']:>2} {row['width']}x{row['height']} {row['resolved_path']} :: {row['pages']}")


if __name__ == '__main__':
    main()
