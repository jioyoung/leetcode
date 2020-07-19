#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (38.50%)
# Likes:    473
# Dislikes: 515
# Total Accepted:    170K
# Total Submissions: 430.6K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
# 
# 
# 
# 
# 
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
# 
# 
# 
# 
# 
# Algorithm of Insertion Sort:
# 
# 
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
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
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        helper = dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur and cur.next:
            '''
            把cur.next插到前面如果它比较小的话
            如果cur.next.val>cur.val 直接下一个
            '''
            val = cur.next.val
            if val > cur.val:
                cur = cur.next
                continue
            if helper.next.val>val:
                helper = dummy
            while helper.next.val < val:
                helper = helper.next
            # 把 cur.next插入helper 和 helper next中间
            new = cur.next
            cur.next = new.next
            new.next = helper.next
            helper.next = new
        return dummy.next
            
        
# @lc code=end

