# -*- coding:utf-8 -*-
#@Time  :    2020/8/21 4:31 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    InversePairs.py
#@Description：

from typing import List

class Solution:
    # 暴力破解法
    def reversePairs_01(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            for j in range(i, length):
                if nums[i] > nums[j]:
                    count += 1
        return count

    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        # 归并的时候，顺便计数
        def merge(nums, start, mid, end, temp):
            i, j = start, mid+1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= end:
                temp.append(nums[j])
                j += 1
            nums[start: end + 1] = temp
            temp.clear()

        def mergeSort(nums, start, end, temp):
            if start >= end:
                return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid+1, end, temp)
            merge(nums, start, mid, end, temp)
        mergeSort(nums, 0, len(nums) - 1, [])

        return self.cnt

if __name__ == '__main__':
    s = Solution()
    nums = [7, 5, 6, 4]
    print(s.reversePairs(nums))