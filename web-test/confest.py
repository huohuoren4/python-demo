from __future__ import annotations
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver | None = None


@pytest.fixture()
def get_driver():
    """获取 driver """
    global driver
    print("\033[31mError:字符串 (~_~)\033[0m")
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://v3.bootcss.com/javascript/#tooltips")
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(5)
        driver.maximize_window()
    yield driver
    driver.quit()