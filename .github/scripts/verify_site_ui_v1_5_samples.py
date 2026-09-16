import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000/"
OUTPUT_DIR = Path("/tmp/site-ui-v1-5")
SAMPLE_PAGES = [
    ("technical-clean", "design_samples/v1.5/technical-clean.html"),
    ("academic-minimal", "design_samples/v1.5/academic-minimal.html"),
    ("modern-dashboard", "design_samples/v1.5/modern-dashboard.html"),
]


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1365,900")
    return webdriver.Chrome(options=options)


def assert_page_has_no_horizontal_overflow(driver, label):
    metrics = driver.execute_script(
        """
        return {
          innerWidth: window.innerWidth,
          documentWidth: document.documentElement.scrollWidth,
          bodyWidth: document.body.scrollWidth
        };
        """
    )
    if metrics["documentWidth"] > metrics["innerWidth"] + 2:
        raise AssertionError(f"horizontal overflow: {label}: {metrics}")
    if metrics["bodyWidth"] > metrics["innerWidth"] + 2:
        raise AssertionError(f"body horizontal overflow: {label}: {metrics}")
    return metrics


def verify_desktop_menu(driver, wait, page, screenshot_name):
    driver.set_window_size(1365, 900)
    driver.get(BASE_URL + page)
    iframe = wait.until(EC.presence_of_element_located((By.ID, "menu")))
    wait.until(lambda d: iframe.get_attribute("scrolling").lower() == "no")

    parent_metrics = driver.execute_script(
        """
        const sub = document.getElementById('sub');
        const menu = document.getElementById('menu');
        return {
          subWidth: sub.getBoundingClientRect().width,
          iframeWidth: menu.getBoundingClientRect().width,
          scrolling: menu.getAttribute('scrolling')
        };
        """
    )
    if abs(parent_metrics["subWidth"] - 180) > 1:
        raise AssertionError(f"desktop #sub width invalid: {page}: {parent_metrics}")
    if abs(parent_metrics["iframeWidth"] - 180) > 1:
        raise AssertionError(f"desktop iframe width invalid: {page}: {parent_metrics}")

    driver.switch_to.frame(iframe)
    clipping = driver.execute_script(
        """
        const width = document.documentElement.clientWidth;
        const visibleLinks = [...document.querySelectorAll('a')].filter(a => {
          const s = getComputedStyle(a);
          const r = a.getBoundingClientRect();
          return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0;
        });
        const bad = visibleLinks.map(a => {
          const r = a.getBoundingClientRect();
          return {text: a.textContent.trim(), left: r.left, right: r.right, width};
        }).filter(x => x.right > x.width + 1 || x.left < -1);
        return {width, scrollWidth: document.documentElement.scrollWidth, bad};
        """
    )
    if clipping["bad"]:
        raise AssertionError(f"desktop menu link clipped: {page}: {clipping['bad'][:8]}")
    driver.switch_to.default_content()
    driver.save_screenshot(str(OUTPUT_DIR / screenshot_name))
    return {"parent": parent_metrics, "menu": clipping}


def verify_mobile_menu(driver, wait):
    driver.set_window_size(390, 900)
    driver.get(BASE_URL + "index.html")
    button = wait.until(EC.element_to_be_clickable((By.ID, "mobile-menu-button")))
    button.click()
    wait.until(lambda d: "mobile-menu-open" in d.find_element(By.TAG_NAME, "body").get_attribute("class"))

    iframe = driver.find_element(By.ID, "menu")
    if iframe.get_attribute("scrolling").lower() != "auto":
        raise AssertionError("mobile iframe scrolling is not auto")

    driver.switch_to.frame(iframe)
    headings = driver.find_elements(By.CSS_SELECTOR, ".sub-text dt")
    heading_metrics = []
    for heading in headings:
        heading_metrics.append(
            driver.execute_script(
                """
                const r = arguments[0].getBoundingClientRect();
                return {text: arguments[0].textContent.trim(), left: r.left, right: r.right, width: r.width, center: r.left + r.width / 2};
                """,
                heading,
            )
        )
    by_text = {item["text"]: item for item in heading_metrics}
    if "メインコンテンツ" not in by_text or "広告" not in by_text:
        raise AssertionError(f"required headings missing: {heading_metrics}")
    main_heading = by_text["メインコンテンツ"]
    ad_heading = by_text["広告"]
    if abs(main_heading["width"] - ad_heading["width"]) > 2:
        raise AssertionError(f"ad heading width differs: {main_heading=} {ad_heading=}")
    if abs(main_heading["center"] - ad_heading["center"]) > 2:
        raise AssertionError(f"ad heading center differs: {main_heading=} {ad_heading=}")

    before = driver.execute_script("return window.scrollY")
    body = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(body).scroll_by_amount(0, 900).perform()
    time.sleep(0.6)
    after = driver.execute_script("return window.scrollY")
    if after <= before + 10:
        raise AssertionError(f"mobile menu did not scroll: {before=} {after=}")

    driver.switch_to.default_content()
    driver.save_screenshot(str(OUTPUT_DIR / "actual-mobile-menu-scrolled.png"))
    return {"mainHeading": main_heading, "adHeading": ad_heading, "scrollBefore": before, "scrollAfter": after}


def verify_revision_history(driver, wait):
    driver.set_window_size(1365, 900)
    driver.get(BASE_URL + "revision_history.html")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.correction-history")))
    result = driver.execute_script(
        """
        const table = document.querySelector('table.correction-history');
        const headers = [...table.querySelectorAll('tr:first-child th')].map(x => x.textContent.trim());
        const rows = [...table.querySelectorAll('tr[data-revision-id]')];
        return {
          headers,
          count: rows.length,
          ids: rows.map(r => r.dataset.revisionId),
          visibleText: table.innerText
        };
        """
    )
    expected_headers = ["No.", "修正種類", "対象", "修正内容"]
    if result["headers"] != expected_headers:
        raise AssertionError(f"revision headers invalid: {result['headers']}")
    if result["count"] != 19:
        raise AssertionError(f"revision row count invalid: {result['count']}")
    if "R-UI-" in result["visibleText"] or "R-FEM" in result["visibleText"]:
        raise AssertionError("internal revision ID is visible")
    driver.save_screenshot(str(OUTPUT_DIR / "revision-history-desktop.png"))
    return result


def verify_samples(driver, wait):
    all_metrics = {}
    for sample_name, relative_url in SAMPLE_PAGES:
        driver.set_window_size(1365, 900)
        driver.get(BASE_URL + relative_url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sample-hero")))
        desktop_metrics = assert_page_has_no_horizontal_overflow(driver, sample_name + " desktop")
        driver.save_screenshot(str(OUTPUT_DIR / f"{sample_name}-desktop.png"))

        driver.set_window_size(390, 900)
        driver.get(BASE_URL + relative_url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sample-hero")))
        mobile_metrics = assert_page_has_no_horizontal_overflow(driver, sample_name + " mobile")
        driver.save_screenshot(str(OUTPUT_DIR / f"{sample_name}-mobile.png"))

        all_metrics[sample_name] = {"desktop": desktop_metrics, "mobile": mobile_metrics}

    driver.set_window_size(1365, 900)
    driver.get(BASE_URL + "design_samples/v1.5/index.html")
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".sample-choice-card")) == 3)
    assert_page_has_no_horizontal_overflow(driver, "sample index desktop")
    hrefs = [element.get_attribute("href") for element in driver.find_elements(By.CSS_SELECTOR, ".sample-choice-card")]
    expected_suffixes = ["technical-clean.html", "academic-minimal.html", "modern-dashboard.html"]
    for suffix in expected_suffixes:
        if not any(href.endswith(suffix) for href in hrefs):
            raise AssertionError(f"sample index link missing: {suffix}")
    driver.save_screenshot(str(OUTPUT_DIR / "design-index-desktop.png"))

    driver.set_window_size(390, 900)
    driver.get(BASE_URL + "design_samples/v1.5/index.html")
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".sample-choice-card")) == 3)
    assert_page_has_no_horizontal_overflow(driver, "sample index mobile")
    driver.save_screenshot(str(OUTPUT_DIR / "design-index-mobile.png"))
    return all_metrics


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    driver = create_driver()
    wait = WebDriverWait(driver, 25)
    try:
        desktop_index = verify_desktop_menu(driver, wait, "index.html", "actual-index-desktop.png")
        desktop_fem = verify_desktop_menu(driver, wait, "fem/fem_7_2_2.html", "actual-fem722-desktop.png")
        mobile_menu = verify_mobile_menu(driver, wait)
        revision = verify_revision_history(driver, wait)
        samples = verify_samples(driver, wait)
    finally:
        driver.quit()

    print("Desktop index menu:", desktop_index)
    print("Desktop FEM menu:", desktop_fem)
    print("Mobile menu:", mobile_menu)
    print("Revision rows:", revision["count"])
    print("Sample metrics:", samples)
    print("site_ui v1.5 visual verification: OK")


if __name__ == "__main__":
    main()
