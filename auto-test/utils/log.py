import logging
import os.path

from main import ROOT_DIR


class Log:
    """
    日志类
    """

    def __init__(self) -> None:
        self.logger = None
        self.file_handler = None
        self.stream_handler = None

    def set_logger(self, log_file: str, fmt: str, log_level: int = logging.INFO) -> None:
        """
        设置 logger
        @param log_file:
        @param fmt: str, 比如: "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
        @param log_level:
        @return:
        """
        self.logger = logging.getLogger()
        self.stream_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler(log_file, 'a', encoding='utf-8')
        self.stream_handler.setLevel(log_level)
        self.set_fmt(fmt)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    def set_logfile(self, log_file: str):
        self.file_handler.stream = open(log_file, 'a')

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


fmt = "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"
log: Log = Log()
log_file = os.path.join(os.path.join(ROOT_DIR, "log"), "2.log")
log.set_logger(log_file, fmt, log_level=logging.WARN)
