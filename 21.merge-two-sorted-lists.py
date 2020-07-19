#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (48.41%)
# Likes:    2647
# Dislikes: 384
# Total Accepted:    685.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummyhead = ListNode(0)
        while l1 and l2:
            if l1.val >=l2.val:
                cur.next = l2
                l2=l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummyhead.next



        # pos = dummyhead =ListNode(0)
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         pos.next = l1
        #         l1=l1.next
        #     else:
        #         pos.next = l2
        #         l2 = l2.next
        #     pos=pos.next
        # if l1:
        #     pos.next = l1
        # else:
        #     pos.next = l2
        # return dummyhead.next
        

