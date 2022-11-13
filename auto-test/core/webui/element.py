from __future__ import annotations

from logging import Logger
from time import sleep

import win32clipboard
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Element(object):

    def __init__(self, driver: WebDriver, log: Logger, sleep_debug: float) -> None:
        self.driver = driver
        self.log = log
        self.sleep_debug = sleep_debug

    def get_url(self, url: str) -> None:
        try:
            self.driver.get(url)
        except TimeoutException:
            msg = "加载页面超时! 页面url: " + url
            self.log.error(msg)
            raise TimeoutException(msg)

    def find_ele_visible(self, value: str, by: str = By.XPATH, timeout: float = 5) -> WebElement:
        """
        定位可见元素, 增加显示等待定位元素, 也可以理解为: 等待元素可见
        状态变化: 元素从不可见到可见
        return: 在指定的时间内, 找到可见元素返回元素对象, 否者报超时错误
        """
        try:
            ele: WebElement = WebDriverWait(self.driver, timeout=timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            msg = "未定位到可见元素 --> %s:%s" % (by, value)
            self.log.error(msg)
            raise TimeoutException(msg)
        return ele

    def wait_ele_invisible(self, value: str, by: str = By.XPATH, timeout: float = 5) -> bool:
        """
        等待元素不可见
        状态变化: 元素从可见到不可见
        return: 在指定的时间内, 元素从可见变成不可见返回 True, 否者报超时错误
        """
        try:
            WebDriverWait(self.driver, timeout=timeout).until_not(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            msg = "元素未消失 --> %s:%s" % (by, value)
            self.log.error(msg)
            raise TimeoutException(msg)
        return True

    def click_ele(self, value: str, by: str = By.XPATH, timeout: float = 5) -> None:
        """
        点击可见元素
        """
        ele = self.find_ele_visible(value=value, by=by, timeout=timeout)
        text = ele.text
        ele.click()
        self.ele_log(action="点击了元素", text=text, by=by, value=value)
        sleep(self.sleep_debug)

    def jsclick_ele(self, value: str, by: str = By.XPATH, timeout: float = 5) -> None:
        """
        js点击可见元素, 通常用于元素上有其他元素遮挡, 比如有弹窗消息之类的元素
        """
        ele = self.find_ele_visible(value=value, by=by, timeout=timeout)
        text = ele.text
        self.driver.execute_script("arguments[0].click();", ele)
        self.ele_log(action="js点击了元素", text=text, by=by, value=value)
        sleep(self.sleep_debug)

    def input_text(self, value: str, text: str, by: str = By.XPATH, timeout: float = 5) -> None:
        """
        先清空输入框, 再输入数据
        """
        ele = self.find_ele_visible(value=value, by=by, timeout=timeout)
        ele.clear()
        ele.send_keys(text)
        self.ele_log(action="输入了文本", text=text, by=by, value=value)

    def get_paste(self) -> str:
        """获取复制的内容"""
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data

    def slide_scrollbar(self, x: int, y: int) -> None:
        """
        滑动滚动条
        x: 正整数--向左, 负整数--向右
        y: 正整数--向上, 负整数--向下
        """
        self.driver.execute_script("window.scrollTo(" + str(x) + ", " + str(y) + ")")

    def ele_log(self, action: str, by: str, value: str, text: str) -> None:
        """
        元素操作日志
        """
        self.log.info("成功%s: %s --> %s:%s", action, text, by, value)
