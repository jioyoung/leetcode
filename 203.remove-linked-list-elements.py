#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        pre = dummy = ListNode(0)
        dummy.next = head
        while head:
            if head.val!=val:
                pre.next = head
                head=head.next
                pre= pre.next
            else:
                head=head.next
        if pre.next:
            pre.next = None
        return dummy.next
                

        
# @lc code=end

