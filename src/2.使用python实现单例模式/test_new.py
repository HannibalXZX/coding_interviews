# -*- coding:utf-8 -*-
#@Time  :    2020/6/22 7:30 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    test_new.py
#@Description：


class A(object):

    # 必须return
    def __new__(cls):
        print("A: __new__()")
        print(cls)
        return 0


    def __init__(self):
        self.val = 3

class B(object):
    def __new__(cls):
        print("B: __new__()")
        print(object.__new__(cls)) # <__main__.B object at 0x10278b4e0>
        return object.__new__(cls)

    def __init__(self):
        self.val = 3



if __name__ == '__main__':
    a = A()
    print(a)

    # AttributeError: 'int' object has no attribute 'val'
    # 因为此时创建的对象是一个int，因此不会再执行A的__init__函数。
    # print(a.val)

    b = B()
    print(b) # <__main__.B object at 0x11010d4e0>
    # 和new里面的
    print(b.val)