# -*- coding:utf-8 -*-
#@Time  :    2020/7/1 7:13 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    cong-wei-dao-tou-da-yin-lian-biao-lcof.py
#@Description： https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 借助栈来实现
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    # 递归
    def reversePrint_1(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head:
            return self.reversePrint_1(head.next) + [head.val]
        else:
            return []


def List2ListNode(head):

    list_ListNode = []
    for i in head:
        listNode = ListNode(i)
        list_ListNode.append(listNode)

    for index in range(len(list_ListNode)):
        if index == len(list_ListNode) - 1:
            break
        list_ListNode[index].next = list_ListNode[index + 1]

    return list_ListNode[0]


if __name__ == '__main__':
    s = Solution()
    list_head = [1, 3, 2]
    head = List2ListNode(list_head)
    print(s.reversePrint_1(head))