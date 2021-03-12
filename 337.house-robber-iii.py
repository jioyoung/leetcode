#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.getRob(root))
        
    def getRob(self, root):    
        if not root:
            return [0, 0]
        left = self.getRob(root.left)
        right = self.getRob(root.right)
        return [root.val + left[1] + right[1], max(left) + max(right)]
        

# @lc code=end

