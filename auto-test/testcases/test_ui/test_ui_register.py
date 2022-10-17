from __future__ import annotations

from time import sleep
import pytest


# 打开注册页面
from page.element import ele


@pytest.fixture(scope="module", autouse=True)
def get_register_page():
    ele.driver.get("https://v5.bootcss.com/")
    sleep(1)


class TestRegister:
    def test_button(self):
        ele.find_ele(value='//*[@id="content"]/div/div/div[2]/div/a[1]').click()
        sleep(3)
