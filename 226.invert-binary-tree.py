#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if not root:
        #     return root
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        
        nodeStack = []
        nodeStack.append(root)
        while nodeStack:
            cur = nodeStack.pop()
            if not cur:
                continue
            
            cur.left, cur.right = cur.right,cur.left
            nodeStack.append(cur.left)
            nodeStack.append(cur.right)
        return root
# @lc code=end

