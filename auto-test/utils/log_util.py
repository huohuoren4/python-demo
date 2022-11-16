import logging
import os.path
import time
from logging import Logger, StreamHandler, FileHandler
from typing import Optional


class LogUtil:
    """
    日志类

    .. 警告::
        不可以重新设置日志的等级和日志的保存目录
    """

    def __init__(self) -> None:
        self.logger: Optional[Logger] = None
        self.file_handler: Optional[StreamHandler] = None
        self.stream_handler: Optional[FileHandler] = None

    def get_logger(self, name: str, log_dir: str, fmt: str, prefix: str = "",
                   log_level: int = logging.INFO) -> Logger:
        """
        获取`Logger`对象

        :param log_dir: 日志目录, 不存在会自动创建
        :param name: 日志对象名字
        :param fmt: 日志格式, 比如: `%(levelname)s\t%(asctime)s\t[%(filename)s:
            %(lineno)d]\t%(message)s`
        :param log_level: 日志等级, 默认为`INFO`
        :param prefix: 日志文件前缀, 比如: webui_202209.log
        :return: 返回一个`Logger`对象
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
        """
        设置日志等级

        常用的日志等级有: `INFO`, `WARNING`, `DEBUG`, `ERROR`

        :param log_level: 日志等级, 默认为`INFO`
        :return:
        """
        self.logger.setLevel(log_level)
        self.file_handler.setLevel(log_level)
        self.stream_handler.setLevel(log_level)

    def set_fmt(self, fmt: str) -> None:
        """
        日志格式

        :param fmt: 日志格式, 比如: `%(levelname)s\t%(asctime)s\t[" + __file__ +"
            %(filename)s:%(lineno)d]\t%(message)s`
        :return:
        """
        log_fmt = logging.Formatter(fmt)
        self.file_handler.setFormatter(log_fmt)
        self.stream_handler.setFormatter(log_fmt)

    def get_log_filename(self) -> str:
        """
        按年月生成日志文件名

        :return: 日志文件名
        """
        local_time = time.time()
        return time.strftime("%Y%m", time.localtime(local_time)) + ".log"
