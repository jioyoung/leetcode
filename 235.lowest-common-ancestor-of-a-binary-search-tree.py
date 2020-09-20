#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        pval, qval = p.val, q.val
        if pval > qval:
            pval, qval = qval, pval
        while 1:
            if qval < root.val:
                root = root.left
            elif pval > root.val:
                root = root.right
            else:
                return root



# @lc code=end

