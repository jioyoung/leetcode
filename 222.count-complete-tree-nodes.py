#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodeQueue = [root]
        count = 0
        while nodeQueue:
            level_len = len(nodeQueue)
            for i in range(level_len):
                node = nodeQueue.pop(0)
                count+=1
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
        return count

        
# @lc code=end

