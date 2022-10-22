import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from core.webui.element import Element
from utils.file_util import deal_path
from utils.log_util import LogUtil

# WebUI 自动化日志
s_fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
webui_log_util = LogUtil()
webui_log_dir = deal_path("log/webui")
webui_log_lever = logging.INFO
webui_log = webui_log_util.get_logger(name="webui", log_dir=webui_log_dir, fmt=s_fmt, prefix="webui_")

# 单个元素对象
s_element = Element()
s_element.driver = webdriver.Chrome()
s_element.web_wait = WebDriverWait(s_element.driver, timeout=5)
s_element.log = webui_log
s_element.driver.set_page_load_timeout(10)
s_element.driver.implicitly_wait(5)
s_element.driver.maximize_window()
