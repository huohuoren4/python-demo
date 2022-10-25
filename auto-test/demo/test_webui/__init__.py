import logging
from selenium import webdriver
from utils.file_util import deal_path
from utils.log_util import LogUtil

# 项目初始化
# WebUI 自动化日志
s_fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
webui_log_util = LogUtil()
webui_log_dir = deal_path("log/webui")
webui_log_lever = logging.INFO
webui_log = webui_log_util.get_logger(name="webui", log_dir=webui_log_dir, fmt=s_fmt, prefix="webui_")

# 单个元素对象
s_driver = webdriver.Chrome()
s_driver.set_page_load_timeout(10)
s_driver.implicitly_wait(5)
s_driver.maximize_window()

# 登录标记
# 未登录就为 False
webui_session = {"is_login": False}
