# coding=utf-8
"""
使用装饰器实现单例模式
"""
from functools import wraps

# 优先进入装饰器
def single_ton(cls):
    _instance = {}

    # 看见@wraps可以保证装饰器修饰的函数的__name__的值保持不变
    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single


@single_ton
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)
    print(s is t)
    print(s.a, t.a)
    print(s.val, t.val)
