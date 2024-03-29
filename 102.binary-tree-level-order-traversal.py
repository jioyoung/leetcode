#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (50.29%)
# Likes:    1839
# Dislikes: 48
# Total Accepted:    445.4K
# Total Submissions: 882.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        分层 树 遍历
        if not root:
            return []
        nodeQueue = [root]
        res = []
        while nodeQueue:
            level_len = len(nodeQueue)
            subList = []
            for i in range(level_len):
                node = nodeQueue.pop(0)
                subList.append(node.val)
                if node.left is not None:
                    nodeQueue.append(node.left)
                if node.right is not None:
                    nodeQueue.append(node.right)
            res.append(subList)
        return res

    #     res = []
    #     self.dfs(root, 0, res)
    #     return res

    # def dfs(self, root, level, res):
    #     if root:
    #         if len(res) < level + 1:
    #             res.append([])
    #         res[level].append(root.val)
    #         self.dfs(root.left, level+1, res)
    #         self.dfs(root.right, level+1, res)

# @lc code=end

