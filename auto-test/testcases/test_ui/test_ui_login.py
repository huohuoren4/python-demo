from __future__ import annotations

import pytest

# 打开登录页面
from core.element import single_ele


@pytest.fixture(scope="module", autouse=True)
def get_login_page():
    try:
        single_ele.driver.get("https://element.eleme.cn/#/zh-CN/component/i18n")
    except:
        single_ele.driver.execute_script('window.stop()')  # 执行Javascript来停止页面加载 window.stop()


class TestLogin:
    def test_tooltip(self):
        single_ele.click_ele(
            value='//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/ul/li[5]/div[6]/ul/li[2]/a')
        single_ele.click_ele(
            value='//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/section/div[1]/div[1]/div/div/div[2]/button[1]')
        is_visible = single_ele.find_ele_visible(value="//div[contains(text(), 'Left Top')]")
        assert is_visible
