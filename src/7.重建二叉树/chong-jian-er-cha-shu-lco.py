# -*- coding:utf-8 -*-
#@Time  :    2020/7/4 11:15 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    chong-jian-er-cha-shu-lco.py
#@Description：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/submissions/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        # 这里可以优化为词典存储，时间复杂度为O(1),详见LeetCode105题
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

