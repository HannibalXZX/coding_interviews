# -*- coding:utf-8 -*-
#@Time  :    2020/7/26 10:42 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    MergeSortedLists.py
#@Description： https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2