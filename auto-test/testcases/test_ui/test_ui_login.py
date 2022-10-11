from __future__ import annotations

from time import sleep

import pytest

# 打开登录页面
from page.element import ele


@pytest.fixture(scope="module", autouse=True)
def get_login_page():
    try:
        ele.driver.get("https://element.eleme.cn/#/zh-CN/component/i18n")
    except:
        ele.driver.execute_script('window.stop()')  # 执行Javascript来停止页面加载 window.stop()
    sleep(1)


class TestLogin:
    def test_tooltip(self):
        ele.find_ele(
            value='//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/ul/li[5]/div[6]/ul/li[2]/a').click()
        ele.find_ele(value='//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/section/div[1]/div[1]/div/div/div[2]/button[1]').click()
        is_visible = ele.wait_ele_visible(value="//div[contains(text(), 'Left Top')]")
        assert is_visible

    def test_tooltip01(self):
        print("执行了 test_tooltip01")
        sleep(3)
