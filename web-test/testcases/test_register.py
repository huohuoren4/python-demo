from __future__ import annotations

from time import sleep
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from page.element import find_ele

driver: WebDriver | None = None


# 打开注册页面
@pytest.fixture(scope="module", autouse=True)
def get_register_page(get_driver):
    global driver
    driver = get_driver
    driver.get("https://v5.bootcss.com/")
    driver.set_page_load_timeout(10)
    sleep(1)


class TestRegister:
    def test_button(self):
        find_ele(driver, value='//*[@id="content"]/div/div/div[2]/div/a[1]').click()
        sleep(3)
