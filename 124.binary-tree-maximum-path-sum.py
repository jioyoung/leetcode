#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (31.07%)
# Likes:    2133
# Dislikes: 164
# Total Accepted:    234.5K
# Total Submissions: 749.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        max_all = [root.val]
        self.getRes(root, max_all)
        return max_all[0]

    def getRes(self, root, max_all):
        if root is None:
            return 0
        left = max(self.getRes(root.left, max_all), 0)
        right = max(self.getRes(root.right, max_all), 0)
        max_cur = root.val + left + right
        if max_cur > max_all[0]:
            max_all[0] = max_cur # max_all is always a list and have only one value
        return root.val + max(left, right)





# @lc code=end

