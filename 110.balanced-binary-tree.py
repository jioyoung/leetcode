#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.79%)
# Likes:    1493
# Dislikes: 135
# Total Accepted:    362.7K
# Total Submissions: 866.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
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
    # 树 balance 左边 右边 深度 差1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth = self.getDepth(root)
        if depth == -1:
            return False
        else:
            return True
        
        
    def getDepth(self, root):
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.getDepth(root.right)
        if right_depth == -1:
            return -1
        if abs(left_depth-right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth)+1
        
# @lc code=end

