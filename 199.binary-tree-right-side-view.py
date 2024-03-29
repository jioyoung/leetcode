#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 最右 树
        # if not root:
        #     return []
        # res = []
        # nodeQueue = [root]
        # while nodeQueue:
        #     level_len = len(nodeQueue)
        #     for i in range(level_len):
        #         node = nodeQueue.pop(0)
        #         if i == level_len-1:
        #             res.append(node.val)
        #         if node.left:
        #             nodeQueue.append(node.left)
        #         if node.right:
        #             nodeQueue.append(node.right)
        # return res
        res = []
        self.getRighest(root, 0, res)
        return res

    def getRighest(self, root, level, res):
        if not root:
            return
        if level == len(res):
            res.append(root.val)
        self.getRighest(root.right, level+1, res)
        self.getRighest(root.left, level+1, res)
        return
        
        
# @lc code=end

