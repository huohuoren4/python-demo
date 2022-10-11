from __future__ import annotations

from time import sleep

import pytest


# 打开登录页面
from page.element import Element


@pytest.fixture(scope="module", autouse=True)
def get_login_page():
    Element.driver.get("https://element.eleme.cn/#/zh-CN/component/i18n")
    sleep(1)

class TestLogin:
    def test_tooltip(self):
        Element.find_ele(value="/html/body/div[2]/div/div[1]/div[7]/div[3]/div/button[1]").click()
        Element.find_ele(value="//div[@class='tooltip fade left in']")
        sleep(3)
