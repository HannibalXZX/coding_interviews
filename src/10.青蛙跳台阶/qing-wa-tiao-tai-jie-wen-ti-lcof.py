# -*- coding:utf-8 -*-
#@Time  :    2020/7/3 7:00 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    qing-wa-tiao-tai-jie-wen-ti-lcof.py
#@Description：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


class Solution(object):
    fibonacci_dic = {}
    def numWays_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 注意：0的时候，为1
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b

        return a % 1000000007

    def numWays(self, n):

        if n in self.fibonacci_dic:
            return self.fibonacci_dic[n]
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n > 1:
            self.fibonacci_dic[n] = self.numWays(n - 1) + self.numWays(n - 2)
            return self.fibonacci_dic[n] % 1000000007


if __name__ == '__main__':
    s = Solution()
    n = 44
    print(s.numWays(n))
    print(s.numWays_1(n))
