#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (34.18%)
# Likes:    1046
# Dislikes: 86
# Total Accepted:    202.9K
# Total Submissions: 592.5K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
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
        slow = dummy = ListNode(0)
        isEqual = False
        fast = head
        while fast and fast.next:
            if fast.val == fast.next.val:
                isEqual = True
                fast = fast.next
            else:
                if isEqual:
                    isEqual = False
                    fast = fast.next
                else:
                    slow.next = fast
                    slow = slow.next
                    fast = fast.next
        if isEqual:
            slow.next = None
        else:
            slow.next = fast
        return dummy.next



                

        
# @lc code=end

