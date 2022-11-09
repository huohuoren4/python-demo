from __future__ import annotations

from logging import Logger
from typing import Optional

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Element(object):

    def __init__(self, driver: WebDriver, log: Logger) -> None:
        self.driver = driver
        self.log = log

    def get_url(self, url: str) -> None:
        try:
            self.driver.get(url)
        except TimeoutException:
            self.log.error("加载页面超时! 页面url: " + url)
            # 执行Javascript来停止页面加载 window.stop()
            self.driver.execute_script('window.stop()')

    def find_ele_visible(self, value: str, by: str = By.XPATH, timeout: float = 5) -> WebElement:
        """
        定位可见元素, 增加显示等待定位元素, 也可以理解为: 等待元素可见
        状态变化: 元素从不可见到可见
        return: 在指定的时间内, 找到可见元素返回元素对象, 否者报超时错误
        """
        try:
            # 屏蔽隐式等待
            self.driver.implicitly_wait(0)
            ele: WebElement = WebDriverWait(self.driver, timeout=timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            msg = "未定位到可见元素 --> %s:%s" % (by, value)
            self.log.error(msg)
            # 打开隐式等待
            self.driver.implicitly_wait(5)
            raise NoSuchElementException(msg)
        # 打开隐式等待
        self.driver.implicitly_wait(5)
        return ele

    def wait_ele_invisible(self, value: str, by: str = By.XPATH, timeout: float = 5) -> bool:
        """
        等待元素不可见
        状态变化: 元素从可见到不可见
        return: 在指定的时间内, 元素从可见变成不可见返回 True, 否者报超时错误
        """
        # 屏蔽隐式等待
        try:
            self.driver.implicitly_wait(0)
            WebDriverWait(self.driver, timeout=timeout).until_not(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            msg = "元素未消失 --> %s:%s" % (by, value)
            self.log.error(msg)
            # 打开隐式等待
            self.driver.implicitly_wait(5)
            raise NoSuchElementException(msg)
        # 打开隐式等待
        self.driver.implicitly_wait(5)
        return True

    def click_ele(self, value: str, by: str = By.XPATH) -> None:
        """
        点击可见元素
        """
        ele = self.find_ele_visible(value=value, by=by)
        text = ele.text
        ele.click()
        self.ele_log(action="点击了元素", text=text, by=by, value=value)

    def jsclick_ele(self, value: str, by: str = By.XPATH) -> None:
        """
        js点击可见元素, 通常用于元素上有其他元素遮挡, 比如有弹窗消息之类的元素
        """
        ele = self.find_ele_visible(value=value, by=by)
        text = ele.text
        self.driver.execute_script("arguments[0].click();", ele)
        self.ele_log(action="js点击了元素", text=text, by=by, value=value)

    def input_text(self, value: str, text: str, by: str = By.XPATH) -> None:
        """
        先清空输入框, 再输入数据
        """
        ele = self.find_ele_visible(value=value, by=by)
        ele.clear()
        ele.send_keys(text)
        self.ele_log(action="输入了文本", text=text, by=by, value=value)

    def ele_log(self, action: str, by: str, value: str, text: str) -> None:
        """
        元素操作日志
        """
        self.log.info("成功%s: %s --> %s:%s", action, text, by, value)
