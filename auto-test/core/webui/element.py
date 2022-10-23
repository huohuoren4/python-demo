from __future__ import annotations

from logging import Logger

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Element(object):

    def __init__(self) -> None:
        self.driver: WebDriver | None = None
        self.web_wait: WebDriverWait | None = None
        self.log: Logger | None = None

    def get_url(self, url: str) -> None:
        try:
            self.driver.get(url)
        except TimeoutException:
            self.log.error("加载页面超时! 页面url: " + url)
            # 执行Javascript来停止页面加载 window.stop()
            self.driver.execute_script('window.stop()')

    def find_ele(self, value: str, by: str = By.XPATH) -> WebElement:
        """
        定位元素, 增加显示等待元素, 元素为可见与不可见都可以定位
        @param value:
        @param by:
        @return:
        """
        try:
            ele = self.web_wait.until(
                expected_conditions.presence_of_element_located((by, value)))
        except TimeoutException:
            msg = "未定位到可见元素 --> %s:%s" % (by, value)
            self.log.error(msg)
            raise NoSuchElementException(msg)
        self.ele_log(ele=ele, action="定位了", by=by, value=value)
        return ele

    def find_ele_visible(self, value: str, by: str = By.XPATH) -> WebElement:
        """
        定位可见元素, 增加显示等待定位元素, 不可见元素不能定位
        @param value:
        @param by:
        @return:
        """
        try:
            ele = self.web_wait.until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            msg = "未定位到可见元素 --> %s:%s" % (by, value)
            self.log.error(msg)
            raise NoSuchElementException(msg)
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
        self.log.info("成功%s元素 --> %s:%s --> 描述:%s%s", action, by, value, action, ele.text)
