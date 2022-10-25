def single_class(cls):
    """单例对象函数"""
    instance = {}

    def single(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return single
