#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (38.53%)
# Likes:    823
# Dislikes: 218
# Total Accepted:    180.5K
# Total Submissions: 467.4K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 分治 切割 链表
        small = dummySmall = ListNode(0)
        large = dummyLarge = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small=small.next
            else:
                large.next = head
                large= large.next
            head = head.next
        small.next = dummyLarge.next
        large.next = None
        return dummySmall.next

# @lc code=end

