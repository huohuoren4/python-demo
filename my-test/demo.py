import json
from abc import abstractmethod, ABCMeta
from typing import Any

from selenium import webdriver


class MetaClass(metaclass=ABCMeta):
    '''类名'''

    @abstractmethod
    def hello(self) -> None: ...


class MyClass(MetaClass):
    '''类名'''

    def hello(self) -> None:
        '''函数说明'''
        print(self.__class__)


class FirstClass(MetaClass):
    '''类名'''

    def hello(self) -> None:
        '''函数说明'''
        print(self.__class__)


class Factory:
    '''类名'''

    def create_class(self, class_name: Any) -> Any:
        '''函数说明'''
        return class_name()


if __name__ == '__main__':
    driver01=webdriver.Chrome()
    driver02=webdriver.Chrome()
