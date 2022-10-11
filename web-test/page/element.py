from __future__ import annotations

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_util import log


class Element(object):
    driver: WebDriver | None = None
    web_wait: WebDriverWait | None = None

    # 定位元素
    @staticmethod
    def find_ele(value: str, by: str = By.XPATH) -> WebElement:
        ele = Element.web_wait.until(
            expected_conditions.presence_of_element_located((by, value)))
        text = ele.text
        if text == "":
            text = ele.get_attribute("innerHTML")
        log.info("成功定位元素 --> %s:%s --> 描述:%s", by, value, text)
        return ele
