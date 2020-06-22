# coding=utf-8
"""
使用__new__实现单例模式
"""

'''
__init__只是负责初始化的函数，真正创建对象的函数是__new__函数
__new__函数是一个类函数，它负责真正的函数创建过程，返回创建的对象。对象创建完毕后，会执行该对象相应的__init__函数。
'''

class SingleTon(object):
    _instance = {}
    print(_instance)
    # __new__()必须要有返回值，返回实例化出来的实例
    def __new__(cls, *args, **kwargs):
        print("SingleTon: __new__()")
        print("cls = {}".format(cls))
        if cls not in cls._instance:
            print("SingleTon里的实例为空")
            cls._instance[cls] = super(SingleTon, cls).__new__(cls)
            # TypeError: object.__new__() takes no arguments
            # cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        else:
            print("SingleTon存在实例")
            print(cls._instance)
        return cls._instance[cls]

# class MyClass(object):
class MyClass(SingleTon):
    class_val = 22

    # 只要写了这个函数，就只有单例 ？？？
    # 调用内部函数会出错
    # def __new__(cls, *args, **kwargs):
    #     print("MyClass: __init__()")
    #     print("cls = {}".format(cls))
    #     print()

    def __init__(self, val):
        print("MyClass: __init__()")
        self.val = val

    def obj_fun(self):
        print(self.val, 'obj_fun')

    @staticmethod
    def static_fun():
        print('staticmethod')

    @classmethod
    def class_fun(cls):
        print(cls.class_val, 'classmethod')


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print(a is b)   # True
    print (id(a), id(b))  # 4367665424 4367665424

    # # 类型验证 ,无论是否是单例，都是一个类型
    print(type(a))  # <class '__main__.MyClass'>
    print(type(b))  # <class '__main__.MyClass'>

    # 实例方法
    a.obj_fun()  # 2 obj_fun
    b.obj_fun()  # 2 obj_fun

    # # 类方法
    MyClass.class_fun()  # 22 classmethod
    a.class_fun()  # 22 classmethod
    b.class_fun()  # 22 classmethod

    # 静态方法
    MyClass.static_fun()  # staticmethod
    a.static_fun()  # staticmethod
    b.static_fun()  # staticmethod

    # 类变量
    a.class_val = 33
    print(MyClass.class_val)  # 22
    print(a.class_val) # 33
    print(b.class_val)  # 33

    # # 实例变量
    # print b.val  # 2
    # print a.val  # 2
