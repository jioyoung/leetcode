#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (52.85%)
# Likes:    1459
# Dislikes: 151
# Total Accepted:    305.3K
# Total Submissions: 575.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 构建binary search tree bst 树 BST
        return self.getTree(nums, 0, len(nums)) 
        # the end is not inclusive
    
    def getTree(self, nums, start, end):
        if start == end:
            return None
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left = self.getTree(nums, start, mid)
        root.right = self.getTree(nums, mid+1, end)
        return root

        
# @lc code=end

