# -*- coding:utf-8 -*-
#@Time  :    2020/6/22 9:37 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    findRepeatNumber.py
#@Description：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/


class Solution:

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int] , 数字在 0～n-1
        :rtype: int
        """
        # 利用数组下标来判断
        for index, num in enumerate(nums):
            while(index != num):
                if num == nums[num]:
                    return num
                else:
                    nums[index], nums[num] = nums[num], nums[index]

    # hash
    def findRepeatNumberI(self, nums):
        """
        :type nums: List[int] , 数字在 0～n-1
        :rtype: int
        """
        list_hash = []  # hash数组
        list_repeat = []         # 重复数组
        for num in nums:
            if num in list_hash:
                list_repeat.append(num)
                return num
            else:
                list_hash.append(num)
        # 超时
        # return list_repeat[0] if list_repeat else None

    # 二分法解决问题
    def findRepeatNumberII(self, nums):
        """
        :type nums: List[int] , 数字在 0～n-1
        :rtype: int
        """
        list_hash = []  # hash数组
        list_repeat = []  # 重复数组
        for num in nums:
            if num in list_hash:
                list_repeat.append(num)
                return num
            else:
                list_hash.append(num)



if __name__ == '__main__':
    s = Solution()
    # list1 = [2, 3, 1, 0, 2, 5, 3]
    # list1 = [1, 0, 1]
    print(s.findRepeatNumber(list1))
