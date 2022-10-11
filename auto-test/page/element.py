from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main import UI_SWITCH
from utils.log_util import log


class Element(object):

    def __init__(self) -> None:
        self.driver: WebDriver = webdriver.Chrome()
        self.web_wait: WebDriverWait = WebDriverWait(self.driver, timeout=5)

    # 定位元素
    def find_ele(self, value: str, by: str = By.XPATH) -> WebElement:
        ele = self.web_wait.until(
            expected_conditions.presence_of_element_located((by, value)))
        text = ele.text
        if text == "":
            text = ele.get_attribute("innerHTML")
        log.info("成功定位元素 --> %s:%s --> 描述:%s", by, value, text)
        return ele

    def wait_ele_visible(self, value: str, by: str = By.XPATH) -> WebElement:
        ele = self.web_wait.until(
            expected_conditions.visibility_of_element_located((by, value)))
        text = ele.text
        if text == "":
            text = ele.get_attribute("innerHTML")
        log.info("成功定位可见元素 --> %s:%s --> 描述:%s", by, value, text)
        return ele


ele = None
# 开启 UI 自动化测试, 设置 UI_SWITCH= True
if UI_SWITCH:
    ele = Element()
