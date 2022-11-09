def single_class(cls):
    """单例对象函数"""
    instance = {}

    def single(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return single


def im(name, age):
    '''外装饰器'''

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            self.driver.implicitly_wait(0)
            res = func(*args, **kwargs)
            return res

        return inner_wrapper

    return wrapper