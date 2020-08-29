# -*- coding:utf-8 -*-
#@Time  :    2020/8/29 10:38 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    LongestSubstringWithoutDup.py
#@Description：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

class Solution:
    # 自己的解法
    # 双指针➕滑动窗口
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        if s == "":
            return 0
        max_sub_str_len = 1
        length = len(s)
        i = 0
        j = 1
        while j < length:
            tmp_max_len = j - i
            if s[j] not in s[i:j]:
                j += 1
                tmp_max_len += 1
                if tmp_max_len > max_sub_str_len:
                    max_sub_str_len = tmp_max_len
            else:
                if i == j:
                    j += 1
                i += 1
                continue
        return max_sub_str_len

    # 哈希表➕双指针
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = {}
        head, res = 0, 0
        for tail in range(n):
            if s[tail] in hashmap:
                head = max(hashmap[s[tail]], head)
            hashmap[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
