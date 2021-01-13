#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (32.47%)
# Likes:    1369
# Dislikes: 97
# Total Accepted:    195.4K
# Total Submissions: 572.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 链表 重新排序 旋转 倒装 链表
        if head is None or head.next is None or head.next.next is None:
            return
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        secondHead = self.reverseList(slow.next)
        slow.next = None
        while secondHead:
            temp1 = head.next
            temp2 = secondHead.next
            head.next = secondHead
            secondHead.next=temp1
            head = temp1
            secondHead=temp2

    def reverseList(self, head):
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
        
# @lc code=end

