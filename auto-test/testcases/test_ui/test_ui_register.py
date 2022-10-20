from __future__ import annotations

from time import sleep
import pytest


# 打开注册页面
from core.element import single_ele


@pytest.fixture(scope="module", autouse=True)
def get_register_page():
    single_ele.driver.get("https://v5.bootcss.com/")
    sleep(1)


class TestRegister:
    def test_button(self):
        single_ele.click_ele(value='//*[@id="content"]/div/div/div[2]/div/a[1]')
        sleep(3)
