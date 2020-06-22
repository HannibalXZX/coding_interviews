## 题目链接 
[LeetCode](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)


## 题目描述（简单）
>请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
```
示例:
现有矩阵 matrix 如下：
输入：s = "We are happy."
输出："We%20are%20happy."
```

## 相关企业


## 思路
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)



时间复杂度：O(n)。遍历字符串 s 一遍。
空间复杂度：O(n)O。额外创建字符数组，长度为 s 的长度的 3 倍。。
