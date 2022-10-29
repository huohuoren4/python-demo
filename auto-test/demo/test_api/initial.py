import logging
from utils.file_util import deal_path, YamlUtil
from utils.log_util import LogUtil

# API 自动化日志初始化
api_log_util = LogUtil()
api_log_dir = deal_path("log/api")
api_log_lever = logging.INFO
s_fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
api_log = api_log_util.get_logger(name="api", log_dir=api_log_dir, fmt=s_fmt, prefix="api_")

# 共享数据
session_data = {"token": "", "expire_time": 0.0}
common_data = YamlUtil("demo/test_api/config/common.yaml").read()