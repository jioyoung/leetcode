#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (43.45%)
# Likes:    939
# Dislikes: 86
# Total Accepted:    369K
# Total Submissions: 848.5K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        if not fast:
            return head
        dummy = slow = ListNode(0)
        slow.next = head

        while fast.next:
            if fast.val != fast.next.val:
                slow.next=fast
                slow = slow.next
            fast = fast.next
        slow.next=fast
        return dummy.next

        
# @lc code=end

