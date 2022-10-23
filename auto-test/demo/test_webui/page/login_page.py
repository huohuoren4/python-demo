from __future__ import annotations

from selenium.common import NoSuchElementException

from core.webui.element import Element
from demo.test_webui import webui_session, webui_log
from utils.file_util import YamlUtil, yaml_variables_substitute

common_data = YamlUtil("demo/test_webui/config/common.yaml").read()
common_page_data = YamlUtil("demo/test_webui/config/page_config/common_page.yaml").read()


class LoginPage:
    def __init__(self) -> None:
        self.element: Element | None = None

    def enter_login_page(self):
        """进入登录页面"""
        if not webui_session["is_login"]:
            self.element.get_url(common_data["项目域名"] + common_page_data["登录页面"]["资源路径"])

    def login_form(self, form_datas: dict, v_data: dict = None) -> None:
        """"""
        if v_data:
            form_datas = yaml_variables_substitute(form_datas, v_data[0])
        self.element.input_text(value=common_page_data["登录页面"]["定位元素"]["用户名输入框"], text=form_datas["用户名"])
        self.element.input_text(value=common_page_data["登录页面"]["定位元素"]["密码输入框"], text=form_datas["密码"])
        self.element.input_text(value=common_page_data["登录页面"]["定位元素"]["验证码输入框"], text=form_datas["验证码"])
        if form_datas["记住我"]:
            self.element.click_ele(value=common_page_data["登录页面"]["定位元素"]["记住我"])
        self.element.click_ele(value=common_page_data["登录页面"]["定位元素"]["登录按钮"])

    def query_error_tip(self, msg: str) -> bool:
        try:
            # 是否进入主页
            self.element.find_ele_visible(value=f'//*[contains(text(),"{msg}")]')
        except NoSuchElementException:
            return False
        return True

    def query_login_success(self):
        try:
            # 是否进入主页
            self.element.find_ele_visible(value=common_page_data["后台主页"]["定位元素"]["侧边栏"]["首页"])
            webui_session["is_login"] = True
            webui_log.info("-------------------- 登录成功 !!! --------------------")
        except NoSuchElementException:
            return False
        return True

    def logout(self):
        if webui_session["is_login"]:
            self.element.get_url(common_data["项目域名"] + common_page_data["后台主页"]["资源路径"])
            self.element.click_ele(common_page_data["后台主页"]["定位元素"]["右上角的个人图标"]["个人图标"])
            self.element.click_ele(common_page_data["后台主页"]["定位元素"]["右上角的个人图标"]["退出登录按钮"])
            webui_session["is_login"] = False
            webui_log.info("-------------------- 退出登录 !!! -----------------------")
