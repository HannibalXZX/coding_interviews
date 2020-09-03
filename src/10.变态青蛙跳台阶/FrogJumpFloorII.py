# -*- coding:utf-8 -*-
#@Time  :    2020/7/3 7:00 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    FrogJumpFloorII.py
#@Description：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


class Solution(object):


    def jumpFloorII(self, number):
        """
        :type n: int
        :rtype: int
        """
        if number == 0 or number == 1:
            return 1
        dp = [0] * (number + 1)
        dp[0] = dp[1] = 1
        for i in range(2, number+1):
            for j in range(0, i):
                dp[i] += dp[j]

        return dp[number]

    def jumpFloorII_1(self, number):
        """
        :type n: int
        :rtype: int
        """
        if number == 0 or number == 1:
            return 1
        dp = [0] * (number + 1)
        dp[0] = dp[1] = 1
        for i in range(2, number + 1):
                dp[i] = dp[i-1] * 2

        return dp[number]


if __name__ == '__main__':
    s = Solution()
    n = 44
    print(s.numWays(n))
    print(s.numWays_1(n))
