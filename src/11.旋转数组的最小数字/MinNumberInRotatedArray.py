# -*- coding:utf-8 -*-
#@Time  :    2020/7/25 6:31 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    MinNumberInRotatedArray.py
#@Description：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

from typing import List
class Solution:
    ## 这里用low有问题，逻辑要更复杂，因为
    def minArray_error(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1]:
            return numbers[0]
        low = 0
        high = len(numbers)-1
        while(low<high):
            mid = (low + high) // 2
            if numbers[mid] > numbers[low]:
                low = mid
            # 这里的逻辑其实是错误的，针对1，2，3，4，5
            elif numbers[mid] < numbers[low]:
                high = mid
            else:
                if numbers[low] == numbers[high]:
                    high -= 1
                elif numbers[low] > numbers[high]:
                    low = mid + 1
                else:
                    break


        return numbers[low]


    def minArray(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1]:
            return numbers[0]
        low = 0
        high = len(numbers)-1
        while(low<high):
            mid = (low + high) // 2
            if numbers[mid] > numbers[high]:
                low=mid+1
            elif numbers[mid] < numbers[high]:
                high=mid
            else:
                # 这里很巧妙
                high -= 1
        return numbers[low]

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while (left < right):
            mid = left + (right - left) // 2
            if rotateArray[right] > rotateArray[mid]:
                right = mid
            elif rotateArray[right] == rotateArray[mid]:
                right = right - 1
            else:
                left = mid + 1
        return rotateArray[left]

    # 这里使用的是low
    def minNumberInRotateArray_2(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        mid = low
        while(rotateArray[low]>= rotateArray[high]):
            mid = low + (high - low)//2
            if high - low == 1:
                mid = high
                break
            if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
                return min(rotateArray[low:high+1])
            elif rotateArray[mid] >= rotateArray[low]:
                low = mid
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid
        return rotateArray[mid]


if __name__ == '__main__':
    s = Solution()
    numbers = [3, 4, 5, 1, 2]
    numbers = [2,2,2,0,1]
    # numbers = [10,1,10,10,10]
    # numbers = [4,5,6,7,0,1,2]
    print(s.minArray_error(numbers))







