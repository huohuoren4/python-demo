from __future__ import annotations

from core.webui.element import Element
from utils.file_util import YamlUtil

common_data = YamlUtil("demo/test_webui/config/common.yaml").read()


class LoginPage:
    def __init__(self) -> None:
        self.element: Element | None = None

    def login(self):
        self.element.get_url(common_data["项目域名"] + common_data["登录页面"]["资源路径"])
        self.element.input_text(value=common_data["登录页面"]["定位元素"]["用户名输入框"], text=common_data["登录页面"]["输入内容"]["用户名"])
        self.element.input_text(value=common_data["登录页面"]["定位元素"]["密码输入框"], text=common_data["登录页面"]["输入内容"]["密码"] )
        self.element.input_text(value=common_data["登录页面"]["定位元素"]["验证码输入框"], text=common_data["登录页面"]["输入内容"]["验证码"])
        self.element.click_ele(value=common_data["登录页面"]["定位元素"]["登录按钮"])

    def logout(self):
        self.element.get_url(common_data["项目域名"] + common_data["后台主页"]["资源路径"])
        self.element.click_ele(common_data["后台主页"])


