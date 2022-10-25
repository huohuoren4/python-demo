from __future__ import annotations

import logging
import os.path
import time
from logging import Logger


class LogUtil:
    """
    日志类
    使用实例:
    fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
    log_util = LogUtil()
    log_dir = os.path.join(ROOT_DIR, "log")
    获取一个logger实例
    log = log_util.get_logger(log_dir, fmt)
    log.warning("weweew")
    """

    def __init__(self) -> None:
        self.logger: logging.Logger | None = None
        self.file_handler: logging.StreamHandler | None = None
        self.stream_handler: logging.FileHandler | None = None

    def get_logger(self, name: str, log_dir: str, fmt: str, prefix: str = "",
                   log_level: int = logging.INFO) -> Logger:
        """
        设置 logger
        @param log_dir:
        @param name: 日志对象名字
        @param fmt: str, 比如: "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
        @param log_level: INFO
        @param prefix: 日志文件前缀, 比如: webui_202209.log
        @return:
        """
        self.logger = logging.getLogger(name=name)
        self.stream_handler = logging.StreamHandler()
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file01 = os.path.join(log_dir, prefix + self.get_log_filename())
        self.file_handler = logging.FileHandler(log_file01, 'a', encoding='utf-8')
        self.set_level(log_level)
        self.set_fmt(fmt)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
        return self.logger

    def set_level(self, log_level: int = logging.INFO) -> None:
        self.logger.setLevel(log_level)
        self.file_handler.setLevel(log_level)
        self.stream_handler.setLevel(log_level)

    def set_fmt(self, fmt: str) -> None:
        """
        日志格式
        @param fmt: str, 比如: "%(levelname)s\t%(asctime)s\t[" + __file__ +"%(filename)s:%(lineno)d]\t%(message)s"
        @return:
        """
        log_fmt = logging.Formatter(fmt)
        self.file_handler.setFormatter(log_fmt)
        self.stream_handler.setFormatter(log_fmt)

    def get_log_filename(self) -> str:
        """
        按年月日生成日志文件名
        @return:
        """
        local_time = time.time()
        return time.strftime("%Y%m", time.localtime(local_time)) + ".log"
