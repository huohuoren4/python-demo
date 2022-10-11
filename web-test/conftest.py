from __future__ import annotations
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page.element import Element


# 获取驱动
@pytest.fixture(scope="session", autouse=True)
def get_driver():
    """获取 driver """
    if Element.driver is None:
        Element.driver = webdriver.Chrome()
        Element.web_wait = WebDriverWait(Element.driver, 5)
        Element.driver.set_page_load_timeout(20)
        Element.driver.implicitly_wait(5)
        Element.driver.maximize_window()
    yield
    Element.driver.quit()
