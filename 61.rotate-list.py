#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (28.04%)
# Likes:    733
# Dislikes: 886
# Total Accepted:    216.3K
# Total Submissions: 770.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 扭曲 move 链表 旋转
        if not head:
            return None
        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        slow = head
        for _ in range(length-k-1):
            slow = slow.next
        newHead = slow.next
        slow.next = None
        tail.next = head
        return newHead
# @lc code=end

