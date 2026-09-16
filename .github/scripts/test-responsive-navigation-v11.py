import json
import re
import shutil
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

ROOT = Path.cwd()
ARTIFACT_DIR = Path('/tmp/v11-smoke')


def heading_position(text, label, start=0):
    pattern = r'^\t\t//' + re.escape(label) + r'\r?$'
    match = re.search(pattern, text[start:], re.M)
    assert match, label
    return start + match.start()


def keep_section(text, start_label, end_label):
    start = heading_position(text, start_label)
    end = heading_position(text, end_label, start + 1)
    return text[start:end]


def verify_static():
    current_bytes = Path('menu.html').read_bytes()
    current = current_bytes.decode('cp932')
    assert current.encode('cp932') == current_bytes

    release_bytes = subprocess.check_output(['git', 'show', 'origin/release_1.0.0:menu.html'])
    release = release_bytes.decode('cp932')

    assert keep_section(current, '表示', '高さ調節') == keep_section(release, '表示', '高さ調節')

    current_height_start = heading_position(current, '高さ調節')
    release_height_start = heading_position(release, '高さ調節')
    current_height_end = current.index('\t//-->', current_height_start)
    release_height_end = release.index('\t//-->', release_height_start)
    assert current[current_height_start:current_height_end] == release[release_height_start:release_height_end]

    href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.I)
    assert href_pattern.findall(current) == href_pattern.findall(release)

    design = json.loads(Path('responsive_navigation_v1.1/responsive_navigation_v1.1_7_detail.json').read_text(encoding='utf-8'))
    css = Path('css/responsive.css').read_text(encoding='utf-8')
    required_ids = []
    for item in design['features'] + design['functions'] + design['variables']:
        if item.get('type') in ('ADD', 'MOD'):
            item_id = item['id']
            if item_id.startswith(('L', 'F', 'T', 'I', 'O', 'V')):
                required_ids.append(item_id)
    source = current + '\n' + css
    missing = [item_id for item_id in required_ids if f'[{item_id}]' not in source]
    assert not missing, missing

    named_functions = re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', current)
    expected_functions = ['Init', 'refreshMobileNavigation', 'updateMobileMenuState', 'disp', 'set_height']
    assert named_functions == expected_functions, named_functions

    assert '@media screen and (max-width: 767px)' in css
    assert '@media screen and (max-width: 768px)' not in css
    assert '@media screen and (min-width: 768px)' in css
    assert 'body.mobile-nav-ready div#sub iframe#menu' in css
    assert 'body.mobile-nav-ready.mobile-menu-open div#sub iframe#menu' in css

    print('Static verification: OK')
    print('KEEP disp(): exact match')
    print('KEEP set_height(): exact match')
    print('Menu href list: exact match')
    print('ADD/MOD traceability IDs:', len(required_ids))


def prepare_test_pages():
    script = r'''
<script type="text/javascript">
window.addEventListener("load", function(){
  window.setTimeout(function(){
    var button = document.getElementById("mobile-menu-button");
    var shouldOpen = window.location.search.indexOf("open=1") >= 0;
    if(button && shouldOpen){button.click();}
    window.setTimeout(function(){
      var buttonAfter = document.getElementById("mobile-menu-button");
      var buttonDisplay = buttonAfter ? window.getComputedStyle(buttonAfter).display : "missing";
      var expanded = buttonAfter ? buttonAfter.getAttribute("aria-expanded") : "missing";
      var viewportWidth = document.documentElement.clientWidth;
      var scrollWidth = document.documentElement.scrollWidth;
      var overflow = scrollWidth > viewportWidth + 1 ? "true" : "false";
      var overflowElements = [];
      var allElements = document.querySelectorAll("body *");
      var elementIndex;
      for(elementIndex = 0; elementIndex < allElements.length; elementIndex++){
        var element = allElements[elementIndex];
        var style = window.getComputedStyle(element);
        if(style.display === "none" || style.visibility === "hidden")continue;
        var rect = element.getBoundingClientRect();
        if(rect.right > viewportWidth + 1){
          overflowElements.push({
            tag: element.tagName,
            id: element.id || "",
            className: typeof element.className === "string" ? element.className : "",
            left: Math.round(rect.left * 10) / 10,
            right: Math.round(rect.right * 10) / 10,
            width: Math.round(rect.width * 10) / 10,
            position: style.position
          });
          if(overflowElements.length >= 30)break;
        }
      }
      document.body.setAttribute("data-test-button-display", buttonDisplay);
      document.body.setAttribute("data-test-expanded", expanded);
      document.body.setAttribute("data-test-overflow", overflow);
      document.body.setAttribute("data-test-client-width", String(viewportWidth));
      document.body.setAttribute("data-test-scroll-width", String(scrollWidth));
      var report = document.createElement("pre");
      report.id = "test-overflow-report";
      report.style.display = "none";
      report.textContent = JSON.stringify(overflowElements);
      document.body.appendChild(report);
    }, 300);
  }, 700);
});
</script>
'''
    pairs = [
        ('index.html', '__test_index.html'),
        ('physics/physics.html', 'physics/__test_physics.html'),
        ('fem/fem.html', 'fem/__test_fem.html'),
    ]
    for source_name, target_name in pairs:
        text = Path(source_name).read_bytes().decode('cp932')
        marker = '</body>'
        index = text.lower().rindex(marker)
        text = text[:index] + script + text[index:]
        Path(target_name).write_bytes(text.encode('cp932'))


def run_chrome(chrome, width, height, url, output_name, screenshot=False):
    common = [
        chrome,
        '--headless',
        '--no-sandbox',
        '--disable-gpu',
        '--disable-dev-shm-usage',
        f'--window-size={width},{height}',
        '--virtual-time-budget=3000',
    ]
    if screenshot:
        output_path = ARTIFACT_DIR / output_name
        command = common + ['--hide-scrollbars', f'--screenshot={output_path}', url]
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        assert output_path.exists() and output_path.stat().st_size > 0
        return

    command = common + ['--dump-dom', url]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output_path = ARTIFACT_DIR / output_name
    output_path.write_bytes(result.stdout)


def read_attrs(name):
    text = (ARTIFACT_DIR / name).read_text(encoding='utf-8')

    def value(attribute):
        match = re.search(attribute + r'="([^"]*)"', text)
        assert match, (name, attribute)
        return match.group(1)

    body_match = re.search(r'<body[^>]*>', text, re.I)
    assert body_match, name
    report_match = re.search(r'<pre id="test-overflow-report"[^>]*>(.*?)</pre>', text, re.I | re.S)
    report = []
    if report_match:
        report = json.loads(unescape(report_match.group(1)))
    return {
        'display': value('data-test-button-display'),
        'expanded': value('data-test-expanded'),
        'overflow': value('data-test-overflow'),
        'clientWidth': value('data-test-client-width'),
        'scrollWidth': value('data-test-scroll-width'),
        'overflowElements': report,
        'body': body_match.group(0),
    }


def assert_no_overflow(name, state):
    if state['overflow'] != 'false':
        print(f"Overflow detected: {name} clientWidth={state['clientWidth']} scrollWidth={state['scrollWidth']}")
        for item in state['overflowElements']:
            print('  ', item)
    assert state['overflow'] == 'false', state


def verify_browser():
    chrome = shutil.which('google-chrome') or shutil.which('google-chrome-stable') or shutil.which('chromium')
    assert chrome, 'Chrome/Chromium not found'
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    prepare_test_pages()

    server = subprocess.Popen(
        [sys.executable, '-m', 'http.server', '8000', '--bind', '127.0.0.1'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(2)
        base = 'http://127.0.0.1:8000/'
        run_chrome(chrome, 375, 812, base + '__test_index.html', 'index-mobile-closed.html')
        run_chrome(chrome, 375, 812, base + '__test_index.html?open=1', 'index-mobile-open.html')
        run_chrome(chrome, 1365, 768, base + '__test_index.html', 'index-desktop.html')
        run_chrome(chrome, 375, 812, base + 'physics/__test_physics.html', 'physics-mobile.html')
        run_chrome(chrome, 375, 812, base + 'fem/__test_fem.html', 'fem-mobile.html')

        closed = read_attrs('index-mobile-closed.html')
        assert closed['display'] not in ('none', 'missing'), closed
        assert closed['expanded'] == 'false', closed
        assert_no_overflow('index-mobile-closed.html', closed)
        assert 'mobile-nav-ready' in closed['body']
        assert 'mobile-menu-open' not in closed['body']

        opened = read_attrs('index-mobile-open.html')
        assert opened['display'] not in ('none', 'missing'), opened
        assert opened['expanded'] == 'true', opened
        assert_no_overflow('index-mobile-open.html', opened)
        assert 'mobile-menu-open' in opened['body']

        desktop = read_attrs('index-desktop.html')
        assert desktop['display'] == 'none', desktop
        assert_no_overflow('index-desktop.html', desktop)

        for name in ('physics-mobile.html', 'fem-mobile.html'):
            state = read_attrs(name)
            assert state['display'] not in ('none', 'missing'), (name, state)
            assert state['expanded'] == 'false', (name, state)
            assert_no_overflow(name, state)

        run_chrome(chrome, 375, 812, base + '__test_index.html', 'index-mobile-closed.png', screenshot=True)
        run_chrome(chrome, 375, 812, base + '__test_index.html?open=1', 'index-mobile-open.png', screenshot=True)
        run_chrome(chrome, 1365, 768, base + '__test_index.html', 'index-desktop.png', screenshot=True)

        print('Mobile closed: OK')
        print('Mobile open: OK')
        print('Desktop hamburger hidden: OK')
        print('Representative page overflow: OK')
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == '__main__':
    verify_static()
    verify_browser()
