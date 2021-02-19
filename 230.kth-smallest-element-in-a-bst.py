#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 中序遍历
        cur = root
        nodeStack = []
        count = 0
        while cur or nodeStack:
            while cur:
                nodeStack.append(cur)
                cur = cur.left
            node = nodeStack.pop()
            count+=1
            if count == k:
                return node.val
            cur = node.right
        

        
# @lc code=end

