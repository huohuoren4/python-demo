

def wrapper_out(name="", age=0):
    '''外装饰器'''
    def wrapper(func):
        '''装饰器'''
        def inner_wrapper(*args, **kwargs):
            '''内装饰器'''
            print("名字: %s, 年龄: %d" % (name, age))
            res = func(*args, **kwargs)
            return res
        return inner_wrapper
    return wrapper

# 类装饰器
class MyPrint:
    '''类名'''
    def __init__(self, name, age) -> None:
        self.name= name
        self.age= age
    def __call__(self, func):
        '''装饰器'''
        def inner_wrapper(*args, **kwargs):
            '''内装饰器'''
            print("名字: %s, 年龄: %d" % (self.name, self.age))
            res = func(*args, **kwargs)
            return res
        return inner_wrapper


