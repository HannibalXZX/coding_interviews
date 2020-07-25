# -*- coding:utf-8 -*-
#@Time  :    2020/7/23 2:08 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    Print1ToMaxOfNDigits.py
#@Description：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
from typing import List


class Solution:
    def printNumbers_1(self, n: int) -> List[int]:

        return [_ for _ in range(1, 10**n)]

    def printNumbers(self, n: int) -> [int]:

        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0':
                    res.append(s)
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        # 规定字符串左边界
        self.start = n - 1
        dfs(0)
        return ','.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(3))


