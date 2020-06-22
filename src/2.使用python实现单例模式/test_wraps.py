# -*- coding:utf-8 -*-
#@Time  :    2020/6/22 8:19 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    test_wraps.py
#@Description：

# 看见@wraps可以保证装饰器修饰的函数的__name__的值保持不变

def is_login(func):
    def foo(*args,**kwargs):
        # print("is_login: ", __name__) # __main__
        print("is_login: ", foo.__name__)
        return func(*args, **kwargs)
    return foo

def is_login_1(func):
    from functools import wraps
    @wraps(func)
    def foo_1(*args, **kwargs):
        print("is_login_1: ", __name__)
        return func(*args, **kwargs)
    return foo_1

def test():
    print("test")
    print('我是：', test.__name__) # test

@is_login
def test1():
    print("test1")
    print('我是：', test1.__name__) # foo


@is_login_1
def test2():
    print("test2")
    print('我是：',test2.__name__) # test2


if __name__ == '__main__':
    # test()
    test1()
    test2()