## 题目链接 
牛客网
<https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/)

## 题目描述（简单）
>写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 
```

## 相关企业


## 思路
### 转换
设跳上 n 级台阶有 f(n) 种跳法。
在所有跳法中，青蛙的最后一步只有两种情况： 
跳上 1 级或 2 级台阶。
* 当为 1 级台阶： 剩 n−1 个台阶，此情况共有 f(n−1) 种跳法；
* 当为 2 级台阶： 剩 n−2 个台阶，此情况共有 f(n−2) 种跳法。

f(n) 为以上两种情况之和，即 f(n)=f(n−1)+f(n−2) ，以上递推性质为斐波那契数列。
本题可转化为 求斐波那契数列第 n 项的值 ，与 面试题10- I. 斐波那契数列 等价，唯一的不同在于起始数字不同。

* 青蛙跳台阶问题：   f(0)=1, f(1)=1, f(2)=2 ；
* 斐波那契数列问题： f(0)=0, f(1)=1, f(2)=1 。

作者：jyd
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 代码

```
记忆化递归
class Solution {
    private int[] memo;

    public int numWays(int n) {
        memo = new int[n + 1];
        Arrays.fill(memo, -1);
        return jump(n);
    }

    private int jump(int n) {
        if (memo[n] != -1) {
            return memo[n];
        }
        if (n == 1 || n == 0) {
            return 1;
        }
        memo[n] = (jump(n - 1) + jump(n - 2)) % 1000_000_007;
        return memo[n];
    }
}
```
