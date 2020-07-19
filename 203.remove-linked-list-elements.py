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
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        if head is None:
            return None
        while head.next is not None:
            if head.val != val:
                pre.next = head
                pre = pre.next
                head = head.next
            else:
                head = head.next
        
        if head.val==val:
            pre.next = None
        else:
            pre.next=head
        
        return dummy.next
                

        
# @lc code=end

