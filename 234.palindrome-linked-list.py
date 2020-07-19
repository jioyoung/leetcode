#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (38.58%)
# Likes:    2821
# Dislikes: 340
# Total Accepted:    394.8K
# Total Submissions: 1M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use slow and fast pointers to reach  the n//2+1
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half 
        newHead = self.reverseListNode(slow)
        while newHead:
            if head.val != newHead.val:
                return False
            head = head.next
            newHead = newHead.next
        return True

    def reverseListNode(self, head):
        if not head:
            return head
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail

# @lc code=end

