# site_navigation v1.6 追加修正記録

更新日: 2026-09-17

## ユーザ指摘
1. v1.6上部メニューの日本語が文字化けする。
2. 右上付近に `文字サイズ / 普通 / 大 / 特大` の切替を追加する。

## 原因
`footer.html` の実ファイルはUTF-8だが、`content-type` metaが `shift_jis` のままであり、footerから読み込むUTF-8 JavaScript内の日本語リテラルがShift_JIS系として解釈される可能性があった。

## 修正
- [MOD] `footer.html`
  - meta charsetをUTF-8へ整合。
  - `site_navigation_v1_6.js` のscript charsetをUTF-8として明示。
  - `site_font_size_v1_6.js` を追加読込。
- [ADD] `js/site_font_size_v1_6.js`
  - [S007] [F007] `registFontSizeControlV16()` を追加。
  - [T008] `updateFontSizeStateV16()` を追加。
  - [T009] `selectStoredFontSizeV16()` を追加。
  - UI日本語はUnicodeエスケープで保持し、親ページの文字コードに依存しない。
  - `localStorage` が利用可能な場合は選択状態を保存する。
- [ADD] `css/site_font_size_v1_6.css`
  - PCではヘッダー右上へ文字サイズ切替を配置。
  - スマホでは固定配置を解除し、ヘッダー内で横幅を圧迫しない位置へ移動。
  - 普通=既存サイズ、大=本文17px程度、特大=本文19px程度を基本とし、見出し・メニューも段階的に拡大する。

## 不変条件
- `menu.html` を変更しない。
- 記事HTMLを変更しない。
- 数式画像、TeX、MathJax内容を変更しない。
- `release_1.0.0` を変更しない。
- 本番FTPへ反映しない。

## 確認
- `site_font_size_v1_6.js` は `node --check` 合格。
- JS内のUI日本語文字列はUnicodeエスケープ化し、非ASCII文字0件を確認。
- 2026-09-17追加差分は `footer.html` と新規JS/CSSの3ファイルのみ。
- 実ブラウザ確認はローカルプレビュー更新後に実施する。
