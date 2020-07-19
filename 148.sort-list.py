#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (37.44%)
# Likes:    2104
# Dislikes: 103
# Total Accepted:    230.4K
# Total Submissions: 586.9K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head = self.mergeSort(head) # mergesort head and head2
        head2 = self.mergeSort(head2)
        return self.merge(head, head2)

    def merge(self, head1, head2):
        pos = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                pos.next = head1
                head1=head1.next
            else:
                pos.next=head2
                head2 = head2.next
            pos = pos.next
        if head1 is None:
            pos.next = head2
        if head2 is None:
            pos.next = head1
        return dummy.next
        
# @lc code=end

