from __future__ import annotations
from time import sleep
import pytest
from page.element import Element
from utils.log_util import log


# 打开登录页面
@pytest.fixture(scope="module", autouse=True)
def get_login_page():
    Element.driver.get("https://auth.huaweicloud.com/authui/login.html#/login")
    sleep(1)


class TestLogin01:
    def test_tooltip(self):
        log.info("hello, world")
        sleep(3)
