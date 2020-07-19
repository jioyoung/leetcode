#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (45.87%)
# Likes:    1401
# Dislikes: 121
# Total Accepted:    356.4K
# Total Submissions: 768.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #exchange cur.next and cur.next.next
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            a.next = b.next
            b.next = a
            cur.next = b
            cur = a
        return dummy.next


        # dummy = ListNode(0)
        # dummy.next = head
        # curr = dummy
        # # change a b, assign the part before a and the part after b
        # while curr.next and curr.next.next:
        #     a = curr.next
        #     b = curr.next.next
        #     a.next = b.next
        #     b.next = a
        #     curr.next = b
        #     curr = a # this is necessary update curr
        # return dummy.next


