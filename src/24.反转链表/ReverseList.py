# -*- coding:utf-8 -*-
#@Time  :    2020/7/26 12:02 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    ReverseList.py
#@Description：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/


class Solution(object):
    # 迭代
    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        pre_node = None

        while(head):
            next_node = head.next
            head.next = pre_node
            pre_node = head
            head = next_node

        return pre_node

    # 递归
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

if __name__ == '__main__':
    s = Solution()
    s.reverseList('')

