# -*- coding:utf-8 -*-
#@Time  :    2020/7/1 8:18 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    fei-bo-na-qi-shu-lie-lcof.py
#@Description：


from functools import lru_cache

class Solution(object):


    def __init__(self):
        self.count=0
        self.fib_dict = {"0": 0, "1": 1}
        self.memo = []

    # 递归法 超时
    '''
    计数结果:
    n=1   count=1
    n=2   count=3
    n=3   count=5
    n=4   count=9   = 3+5 + 1
    n=5   count=15  = 9+5 + 1
    n=10  count=177
    n=20  count=21891
    '''
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            self.count += 1
            return 0
        elif n == 1:
            self.count += 1
            return 1
        elif n > 1:
            self.count += 1
            return (self.fib(n-1) + self.fib(n-2)) % 1000000007
        else:
            return None


    # 记忆递归法形式1,count为n-1
    def fib_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            self.count += 1
            return self.fib_dict["0"]
        elif n == 1:
            self.count += 1
            return self.fib_dict["1"]
        elif n > 1:
            # 先检查下数组有没有值
            self.count += 1
            if str(n) in self.fib_dict:
                # print(n)
                fib_n = self.fib_dict[str(n)]
            else:
                if str(n-1) in self.fib_dict:
                    # print(n-1)
                    fib_n_1 = self.fib_dict[str(n-1)]
                else:
                    fib_n_1 = self.fib_1(n-1)
                    self.fib_dict[str(n-1)] = fib_n_1

                if str(n - 2) in self.fib_dict:
                    print(n - 2)
                    fib_n_2 = self.fib_dict[str(n - 2)]
                else:
                    fib_n_2 = self.fib_1(n - 2)
                    self.fib_dict[str(n - 2)] = fib_n_2

                fib_n = fib_n_1 + fib_n_2

                self.fib_dict[str(n)] = fib_n
            return fib_n % 1000000007

    # 动态规划法
    def fib_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


    # 记忆递归法形式2
    def jump(self, n):

        if (self.memo[n] != -1):
            return self.memo[n]

        if n == 1:
            return 1

        if n == 0:
            return 0

        self.memo[n] = (self.jump(n-1) + self.jump(n-2)) % 1000000007

        return self.memo[n]

    # 记忆递归法
    def fib_3(self, n):
        self.memo = [-1 for _ in range(n+1)]
        return self.jump(n)

    # ru_cache可以记录函数的调用结果，再次使用时直接使用之前的返回值，而不真的再次调用。
    # 缓存装饰器
    @lru_cache(maxsize=None)
    def fib_4(self, n: int) -> int:
        if n < 2:
            return n
        return (self.fib_4(n - 1) + self.fib_4(n - 2)) % 1000000007

if __name__ == '__main__':
    s = Solution()
    n = 500
    # print(s.fib(n))
    # print(s.count)
    # s.count = 0
    print(s.fib_4(n))
    # print(s.count)
    # s.fib_2(n)