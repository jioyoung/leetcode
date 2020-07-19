#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (42.67%)
# Likes:    1267
# Dislikes: 74
# Total Accepted:    196.4K
# Total Submissions: 458.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if head.next is None:
            return TreeNode(head.val)
        return self.getBST(head, None)

    def getBST(self, head, tail):
        if head== tail:
            return None
        slow = head
        fast = head
        while fast !=tail and fast.next!=tail:
            slow = slow.next
            fast = fast.next.next
        # root is slow
        root = TreeNode(slow.val)
        root.left = self.getBST(head, slow)
        root.right = self.getBST(slow.next, tail)
        return root
        
# @lc code=end

