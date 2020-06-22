# -*- coding:utf-8 -*-
#@Time  :    2020/6/22 11:01 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    replaceSpace.py
#@Description：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/


class Solution(object):

    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not isinstance(s,str) and s:
            return


        return s.replace(" ", "%20")



if __name__ == '__main__':
    solution = Solution()
    s = "We are happy"
    print(solution.replaceSpace(s))