import logging
from selenium import webdriver
from utils.file_util import deal_path
from utils.log_util import LogUtil

# 项目初始化
# 操作可见元素的等待时间, 集中在点击事件
sleep_debug = 0

# WebUI 自动化日志
s_fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
webui_log_dir = deal_path("log/webui")
webui_log_lever = logging.INFO
webui_log_util = LogUtil(name="webui", log_dir=webui_log_dir, fmt=s_fmt, prefix="webui_")
webui_log = webui_log_util.get_logger()

# 谷歌驱动对象
s_driver = webdriver.Chrome()
s_driver.set_page_load_timeout(20)
s_driver.implicitly_wait(1)
s_driver.maximize_window()

# 登录标记
# 未登录就为 False
webui_session = {"is_login": False}
