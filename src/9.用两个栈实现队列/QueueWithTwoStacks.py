# -*- coding:utf-8 -*-
#@Time  :    2020/7/1 8:01 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    QueueWithTwoStacks.py
#@Description：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/


class CQueue(object):

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.A.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


if __name__ == '__main__':
    value = 2
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    obj.appendTail(value)
    obj.appendTail(3)
    obj.appendTail(4)
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(obj.deleteHead())
    print(obj.deleteHead())
    # param_2 = obj.deleteHead()