# -*- coding:utf-8 -*-
class Solution:

    ## 装饰器
    def Power(self, base, exponent):
        # write code here
        if abs(base - 0)<1e-7 and exponent < 0:
            return 0
        absExponent = abs(exponent)

        def PowerWithUnsigned(base,exponent):
            if exponent == 0:
                return 1
            if exponent == 1:
                return base
            result = PowerWithUnsigned(base, exponent>>1)
            result *= result
            if exponent & 1 == 1:
                result *= base
            return result

        result = PowerWithUnsigned(base, absExponent)
        if exponent < 0:
            result = 1/result
        return result

    def myPow_1(self, x: float, n: int) -> float:
        return pow(x, n)

    def myPow(self, x: float, n: int) -> float:
        ## 设立初始条件
        if abs(x-0)<1e-7 and n <0:
            return 0
        abs_n = abs(n)

        def PowerWithUnsigned(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            result = self.myPow(x, n >> 1)
            result *= result
            if n & 1 == 1:
                result *= x
            return result

        result = PowerWithUnsigned(x, abs_n)
        if n < 0:
            result = 1/result

        return result

    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)





if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.10000,3))