from __future__ import annotations

from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from page.element import find_ele

driver: WebDriver | None = None


# 打开登录页面
@pytest.fixture(scope="module", autouse=True)
def get_login_page(get_driver):
    global driver
    driver = get_driver
    driver.get("https://element.eleme.cn/#/zh-CN/component/i18n")
    sleep(1)

class TestLogin:
    def test_tooltip(self):
        find_ele(driver, value="/html/body/div[2]/div/div[1]/div[7]/div[3]/div/button[1]").click()
        find_ele(driver, value="//div[@class='tooltip fade left in']")
        sleep(3)
