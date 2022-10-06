
class MyClass:
    '''类名'''

    def __init__(self, data, step) -> None:
        self.__data = data
        self.__step = step

    @property
    def data(self):
        '''函数说明'''
        return self.__data

    @data.setter
    def data(self, data):
        '''函数说明'''
        self.__data = data

    @property
    def step(self):
        '''函数说明'''
        return self.__step

    @step.setter
    def step(self, step):
        '''函数说明'''
        self.__step = step

    def __getitem__(self, item):
        return self.__data[item]



if __name__ == '__main__':
    li = [1, 2, 3, 10, 20]
    cls = MyClass(li, 0)
    for val in cls:
       print(val)

