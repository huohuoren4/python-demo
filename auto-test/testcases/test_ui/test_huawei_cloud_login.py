from __future__ import annotations
import pytest
from core.element import single_ele


# 打开登录页面
@pytest.fixture(scope="module", autouse=True)
def get_login_page():
    single_ele.driver.get("https://auth.huaweicloud.com/authui/login.html#/login")


class TestHuaweiCloudLogin:
    def test_login(self):
        single_ele.click_ele(value='//*[@id="IAMLinkDiv"]/span')
        single_ele.input_text(value='//*[@id="IAMAccountInputId"]', text="hid_tt-c4y5905k9xko")
        single_ele.input_text(value='//*[@id="IAMUsernameInputId"]', text="huohuoren4")
        single_ele.input_text(value='//*[@id="IAMPasswordInputId"]', text="Wang678994")
        single_ele.click_ele(value='//*[@id="btn_submit"]')
