#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (36.12%)
# Likes:    1496
# Dislikes: 105
# Total Accepted:    218.6K
# Total Submissions: 603.6K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = dummyHead
        if m == n:
            return dummyHead.next
        while head:
            if count < m:
                head = head.next
                slow = slow.next
                count += 1
            elif count == m:
                left = slow
                right = head
                count+=1
                head = head.next
                slow = slow.next
            elif count > m and count < n:
                temp = head.next
                head.next = slow
                slow = head
                head = temp
                count+=1
            elif count == n:
                right.next = head.next
                left.next = head
                head.next = slow
                break
        return dummyHead.next

# @lc code=end

