import os.path

import pytest


class Animal(object):
    '''类名'''

    def __init__(self, color: str, name: str) -> None:
        self.color= color
        self.name= name

    def bark(self) -> None :
        print("动物在叫")

    class Meta:
        verbose_name= "补充内容"


class Dog(Animal):
    '''类名'''

    @pytest.mark.dependency()
    def bark(self) -> None :
        print("小狗在叫")


    def drink(self) -> None :
        print("小狗在喝水")


if __name__ == '__main__':
    dog01= Dog("1", "2")
    dog02= dog01
    dog02.name= "1111"
    print(dog01.name)

























