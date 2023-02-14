import logging
import os.path
import time
from logging import Logger


class LogUtil:
    """
    日志配置类
    """

    def __init__(self, name: str, log_dir: str, fmt: str, prefix: str = "",
                 log_level: int = logging.INFO) -> None:
        """
        获取`Logger`对象初始化

        :param log_dir: 日志目录, 不存在会自动创建
        :param name: 日志对象名字
        :param fmt: 日志格式, 比如: `%(levelname)s\t%(asctime)s\t[%(filename)s:
            %(lineno)d]\t%(message)s`
        :param log_level: 日志等级, 默认为`INFO`
        :param prefix: 日志文件前缀, 比如: webui_202209.log
        :return: 返回一个`Logger`对象
        """
        self._logger = logging.getLogger(name=name)
        self._stream_handler = logging.StreamHandler()
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file01 = os.path.join(log_dir, prefix + self._get_log_filename())
        self._file_handler = logging.FileHandler(log_file01, 'a', encoding='utf-8')
        self.set_level(log_level)
        self.set_fmt(fmt)
        self._logger.addHandler(self._file_handler)
        self._logger.addHandler(self._stream_handler)

    def get_logger(self) -> Logger:
        """
        获取`Logger`对象

        :return: 返回一个`Logger`对象
        """
        return self._logger

    def set_level(self, log_level: int = logging.INFO) -> None:
        """
        设置日志等级

        常用的日志等级有: `INFO`, `WARNING`, `DEBUG`, `ERROR`

        :param log_level: 日志等级, 默认为`INFO`
        :return:
        """
        self._logger.setLevel(log_level)
        self._file_handler.setLevel(log_level)
        self._stream_handler.setLevel(log_level)

    def set_filestream(self, log_dir: str, prefix: str = "") -> None:
        """
        修改日志文件的目录

        :param log_dir: 
        :param prefix:
        :return:
        """
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file01 = os.path.join(log_dir, prefix + self._get_log_filename())
        self._file_handler.setStream(open(log_file01, "a", encoding='utf-8'))

    def set_fmt(self, fmt: str) -> None:
        """
        日志格式

        :param fmt: 日志格式, 比如: `%(levelname)s\t%(asctime)s\t[" + __file__ +"
            %(filename)s:%(lineno)d]\t%(message)s`
        :return:
        """
        log_fmt = logging.Formatter(fmt)
        self._file_handler.setFormatter(log_fmt)
        self._stream_handler.setFormatter(log_fmt)

    def _get_log_filename(self) -> str:
        """
        按年月生成日志文件名

        :return: 日志文件名
        """
        local_time = time.time()
        return time.strftime("%Y%m", time.localtime(local_time)) + ".log"

