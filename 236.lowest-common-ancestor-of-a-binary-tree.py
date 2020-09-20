#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        leftCommonAncestor = self.lowestCommonAncestor(root.left, p,q)
        rightCommonAncestor = self.lowestCommonAncestor(root.right, p,q)
        if leftCommonAncestor is None:
            return rightCommonAncestor
        if rightCommonAncestor is None:
            return leftCommonAncestor
        return root      
# @lc code=end

