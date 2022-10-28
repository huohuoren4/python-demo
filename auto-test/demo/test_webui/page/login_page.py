from logging import Logger
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from core.webui.element import Element
from demo.test_webui import webui_session
from utils.file_util import yaml_variables_substitute


class LoginPage(Element):

    def __init__(self, driver: WebDriver, log: Logger, common_data: dict,
                 common_page_data: dict, timeout: float = 5) -> None:
        super().__init__(driver, timeout, log)
        self.common_data = common_data
        self.common_page_data = common_page_data

    def enter_login_page(self):
        """进入登录页面"""
        if not webui_session["is_login"]:
            self.get_url(self.common_data["项目域名"] + self.common_page_data["登录页面"]["资源路径"])

    def login_form(self, form_datas: dict, v_data: dict = None) -> None:
        """登录表单"""
        if v_data:
            form_datas = yaml_variables_substitute(form_datas, v_data[0])
        self.input_text(value=self.common_page_data["登录页面"]["定位元素"]["用户名输入框"], text=form_datas["用户名"])
        self.input_text(value=self.common_page_data["登录页面"]["定位元素"]["密码输入框"], text=form_datas["密码"])
        self.input_text(value=self.common_page_data["登录页面"]["定位元素"]["验证码输入框"], text=form_datas["验证码"])
        if form_datas["记住我"]:
            self.click_ele(value=self.common_page_data["登录页面"]["定位元素"]["记住我"])
        # sleep(0.5)
        self.click_ele(value=self.common_page_data["登录页面"]["定位元素"]["登录按钮"])

    def query_error_tip(self, msg: str) -> bool:
        """查询错误提示"""
        try:
            # 是否进入主页
            self.find_ele_visible(value=f'//*[contains(text(),"{msg}")]')
        except NoSuchElementException:
            return False
        return True

    def query_login_success(self) -> bool:
        """查询登录成功"""
        try:
            # 是否进入主页
            self.find_ele_visible(value=self.common_page_data["后台主页"]["定位元素"]["侧边栏"]["首页"])
            webui_session["is_login"] = True
            self.log.info("-------------------- 登录成功 !!! --------------------")
        except NoSuchElementException:
            return False
        return True

    def logout(self) -> None:
        """用户登出"""
        if webui_session["is_login"]:
            self.get_url(self.common_data["项目域名"] + self.common_page_data["后台主页"]["资源路径"])
            self.click_ele(self.common_page_data["后台主页"]["定位元素"]["右上角的个人图标"]["个人图标"])
            self.click_ele(self.common_page_data["后台主页"]["定位元素"]["右上角的个人图标"]["退出登录按钮"])
            webui_session["is_login"] = False
            self.log.info("-------------------- 退出登录 !!! -----------------------")
