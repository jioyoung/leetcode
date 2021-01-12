#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.14%)
# Likes:    5207
# Dislikes: 1339
# Total Accepted:    880.6K
# Total Submissions: 2.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check if the sum is greater than 9
        # iterate until one list is empty
        remain = 0
        value = 0
        head = dummy = ListNode(0)
        while l1 or l2:
            value = remain # this update is important 
            if l1:
                value+=l1.val
                l1=l1.next
            if l2:
                value+=l2.val
                l2=l2.next
            if value > 9:
                remain = 1
                value-=10
            else:
                remain = 0
            head.next = ListNode(value)
            head = head.next
        if remain == 1:
            head.next = ListNode(1)
        return dummy.next

                
               

