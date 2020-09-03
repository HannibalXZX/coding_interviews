# -*- coding:utf-8 -*-
#@Time  :    2020/8/28 10:00 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    getKthFromEnd.py
#@Description：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i = j = head

        # 这里要考虑k大于链表的长度
        while k:
            if j:
                j = j.next
                k -= 1
            else:
                return None

        while j:
            i = i.next
            j = j.next

        return i




