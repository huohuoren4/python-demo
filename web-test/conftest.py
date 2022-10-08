from __future__ import annotations
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver | None = None

# 获取驱动
@pytest.fixture(scope="session")
def get_driver():
    """获取 driver """
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(5)
        driver.maximize_window()
    yield driver
    driver.quit()
