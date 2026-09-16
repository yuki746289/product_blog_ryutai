import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000/"
OUTPUT_DIR = Path("/tmp/site-ui-v1-4")
MATH_PAGES = [
    "fem/fem_6_2_6.html",
    "fem/fem_7_1_1.html",
    "fem/fem_7_1_2.html",
    "fem/fem_7_2_1.html",
    "fem/fem_7_2_2.html",
]


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=390,1000")
    return webdriver.Chrome(options=options)


def assert_white(value: str, label: str) -> None:
    allowed = {"rgb(255, 255, 255)", "rgba(255, 255, 255, 1)"}
    if value not in allowed:
        raise AssertionError(f"{label} is not white: {value}")


def verify_mobile_menu(driver, wait) -> None:
    driver.set_window_size(390, 1000)
    driver.get(BASE_URL + "index.html")
    wait.until(EC.presence_of_element_located((By.ID, "mobile-menu-button")))
    if "修正履歴はこちら" not in driver.page_source:
        raise AssertionError("top-page revision-history notice missing")
    driver.save_screenshot(str(OUTPUT_DIR / "index-mobile-closed.png"))

    button = driver.find_element(By.ID, "mobile-menu-button")
    button.click()
    wait.until(lambda d: "mobile-menu-open" in d.find_element(By.TAG_NAME, "body").get_attribute("class"))

    iframe = driver.find_element(By.ID, "menu")
    if iframe.get_attribute("scrolling").lower() != "auto":
        raise AssertionError("menu iframe scrolling is not auto")
    iframe_background = driver.execute_script("return getComputedStyle(arguments[0]).backgroundColor", iframe)
    assert_white(iframe_background, "menu iframe")
    driver.save_screenshot(str(OUTPUT_DIR / "index-mobile-menu-top.png"))

    driver.switch_to.frame(iframe)
    body_background = driver.execute_script("return getComputedStyle(document.body).backgroundColor")
    wrapper_background = driver.execute_script(
        "return getComputedStyle(document.getElementById('sub-wrapper')).backgroundColor"
    )
    assert_white(body_background, "menu body")
    assert_white(wrapper_background, "menu wrapper")

    first_links = driver.find_elements(By.CSS_SELECTOR, "#sub-menu > ul:first-of-type li a")
    link_texts = [element.text.strip() for element in first_links]
    favorite_index = link_texts.index("お気に入りに追加")
    history_index = link_texts.index("修正履歴")
    if history_index != favorite_index + 1:
        raise AssertionError(f"revision-history link position invalid: {link_texts}")

    scroll_height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)"
    )
    inner_height = driver.execute_script("return window.innerHeight")
    if scroll_height <= inner_height + 100:
        raise AssertionError(f"menu content is not scrollable: {scroll_height=} {inner_height=}")

    before_y = driver.execute_script("return window.scrollY")
    body = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(body).scroll_by_amount(0, 700).perform()
    time.sleep(0.8)
    after_y = driver.execute_script("return window.scrollY")
    if after_y <= before_y + 10:
        raise AssertionError(f"wheel scroll did not move menu: before={before_y}, after={after_y}")

    driver.switch_to.default_content()
    driver.save_screenshot(str(OUTPUT_DIR / "index-mobile-menu-scrolled.png"))


def verify_math_layout(driver, wait) -> None:
    driver.set_window_size(390, 1000)
    all_metrics = {}
    for page in MATH_PAGES:
        driver.get(BASE_URL + page)
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "mjx-container")) > 0)
        time.sleep(1.2)
        metrics = driver.execute_script(
            """
            const bad = [];
            document.querySelectorAll('.math-block').forEach((block, index) => {
              const math = block.querySelector('mjx-container[display="true"]');
              if (!math) return;
              const blockRect = block.getBoundingClientRect();
              const mathRect = math.getBoundingClientRect();
              if (mathRect.right > blockRect.right + 2 || mathRect.left < blockRect.left - 2) {
                bad.push({
                  index,
                  blockWidth: blockRect.width,
                  mathWidth: mathRect.width,
                  leftOverflow: blockRect.left - mathRect.left,
                  rightOverflow: mathRect.right - blockRect.right
                });
              }
            });
            return {
              bad,
              docScrollWidth: document.documentElement.scrollWidth,
              innerWidth: window.innerWidth
            };
            """
        )
        all_metrics[page] = metrics
        if metrics["docScrollWidth"] > metrics["innerWidth"] + 2:
            raise AssertionError(f"page horizontal overflow: {page}: {metrics}")
        if metrics["bad"]:
            raise AssertionError(f"math block overflow: {page}: {metrics['bad'][:10]}")

    driver.get(BASE_URL + "fem/fem_7_2_2.html")
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "mjx-container")) > 0)
    time.sleep(1)
    driver.save_screenshot(str(OUTPUT_DIR / "fem722-mobile.png"))
    print("Mobile formula metrics:", all_metrics)


def verify_desktop(driver, wait) -> None:
    driver.set_window_size(1365, 900)
    driver.get(BASE_URL + "index.html")
    wait.until(EC.presence_of_element_located((By.ID, "menu")))
    driver.save_screenshot(str(OUTPUT_DIR / "index-desktop.png"))

    driver.get(BASE_URL + "fem/fem_7_2_2.html")
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "mjx-container")) > 0)
    time.sleep(1)
    driver.save_screenshot(str(OUTPUT_DIR / "fem722-desktop.png"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    driver = create_driver()
    wait = WebDriverWait(driver, 25)
    try:
        verify_mobile_menu(driver, wait)
        verify_math_layout(driver, wait)
        verify_desktop(driver, wait)
    finally:
        driver.quit()
    print("site_ui v1.4 browser verification: OK")


if __name__ == "__main__":
    main()
