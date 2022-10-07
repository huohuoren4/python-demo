import os.path


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

    def bark(self) -> None :
        print("小狗在叫")


    def drink(self) -> None :
        print("小狗在喝水")


if __name__ == '__main__':
    print("12jorewoeow3".replace("/", "123"))
    print(os.path.split(__file__))

























