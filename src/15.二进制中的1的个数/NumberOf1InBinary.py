# -*- coding:utf-8 -*-
#@Time  :    2020/7/22 5:51 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    15_NumberOf1InBinary.py
#@Description：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

class Solution:
    def hammingWeight_1(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1

        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(3))