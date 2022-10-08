from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_util import log


# 定位元素
def find_ele(driver: WebDriver, value: str, by: str = By.XPATH, timeout: float = 5) -> WebElement:
    ele = WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_element_located((by, value)))
    log.info("成功定位元素 --> %s:%s descriptiont: %s", by, value, ele.get_attribute("innerHTML"))
    return ele
