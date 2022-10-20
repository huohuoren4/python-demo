from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main import UI_SWITCH
from utils.log_util import single_log


class Element(object):

    def __init__(self) -> None:
        self.driver: WebDriver = webdriver.Chrome()
        self.web_wait: WebDriverWait = WebDriverWait(self.driver, timeout=5)

    def find_ele(self, value: str, by: str = By.XPATH) -> WebElement:
        """
        定位元素, 增加显示等待元素, 元素为可见与不可见都可以定位
        @param value:
        @param by:
        @return:
        """
        ele = self.web_wait.until(
            expected_conditions.presence_of_element_located((by, value)))
        self.ele_log(ele=ele, action="定位了", by=by, value=value)
        return ele

    def find_ele_visible(self, value: str, by: str = By.XPATH) -> WebElement:
        """
        定位可见元素, 增加显示等待定位元素, 不可见元素不能定位
        @param value:
        @param by:
        @return:
        """
        ele = self.web_wait.until(
            expected_conditions.visibility_of_element_located((by, value)))
        self.ele_log(ele=ele, action="定位了", by=by, value=value)
        return ele

    def click_ele(self, value: str, by: str = By.XPATH) -> None:
        """
        点击可见元素
        @param value:
        @param by:
        @return:
        """
        ele = self.find_ele_visible(value=value, by=by)
        self.ele_log(ele=ele, action="点击了", by=by, value=value)
        ele.click()

    def jsclick_ele(self, value: str, by: str = By.XPATH) -> None:
        """
        js点击可见元素, 通常用于元素上有其他元素遮挡, 比如有弹窗消息之类的元素
        @param value:
        @param by:
        @return:
        """
        ele = self.find_ele_visible(value=value, by=by)
        self.ele_log(ele=ele, action="js点击了", by=by, value=value)
        self.driver.execute_script("arguments[0].click();", ele)

    def input_text(self, value: str, text: str, by: str = By.XPATH) -> None:
        """
        先清空输入框, 再输入数据
        @param value:
        @param text:
        @param by:
        @return:
        """
        ele = self.find_ele_visible(value=value, by=by)
        ele.clear()
        self.ele_log(ele=ele, action="输入了" + text + "到", by=by, value=value)
        ele.send_keys(text)

    def ele_log(self, ele: WebElement, action: str, by: str, value: str) -> None:
        """
        元素操作日志
        self.ele_log(ele=ele, action="输入了" + text + "到", by=by, value=value)
        注意: 日志输出代码要在元素操作代码的前面
        ele.send_keys(text)
        @param ele:
        @param action:
        @param by:
        @param value:
        @return:
        """
        text = ele.text
        if text == "":
            text = ele.get_attribute("innerHTML")
        single_log.info("成功%s元素 --> %s:%s --> 描述:%s%s", action, by, value, action, text)


# 单例对象
single_ele = None
# 开启 UI 自动化测试, 设置 UI_SWITCH= True
if UI_SWITCH:
    single_ele = Element()
