# -*- coding:utf-8 -*-
#@Time  :    2020/6/22 9:37 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    findNumberIn2DArray.py
#@Description：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

class Solution(object):

    # 不断缩小矩阵
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        max_row = len(matrix)
        max_column = len(matrix[0])
        row = 0
        colunm = max_column - 1

        while(matrix and row<max_row and colunm>=0):
            tmp = matrix[row][colunm]
            if tmp == target:
                return True
            elif tmp < target:
                row += 1
            else:
                colunm -= 1

        return False



if __name__ == '__main__':
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    matrix_1 = [
        [1, 4, 7, 11, 15],
    ]

    matrix_2 = [
        [1],
    ]
    s = Solution()
    print(s.findNumberIn2DArray(matrix, 20))
    print(s.findNumberIn2DArray(matrix_1, 1))
    print(s.findNumberIn2DArray(matrix_2, 1))







