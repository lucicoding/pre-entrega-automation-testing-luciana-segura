import os
from datetime import datetime
import pytest
import pytest_html
from selenium import webdriver
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{fecha}.png")
            driver.save_screenshot(screenshot_path)
            extra = getattr(rep, "extra", [])
            extra.append(pytest_html.extra.screenshot(screenshot_path))
            rep.extra = extra
            print(f"Captura de pantalla guardada en: {screenshot_path}")