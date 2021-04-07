#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (35.93%)
# Likes:    870
# Dislikes: 488
# Total Accepted:    331.9K
# Total Submissions: 921.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 树 分层 最小深度
        if not root:
            return 0
        depth = 0
        nodeQueue = [root]
        while nodeQueue:
            level_len = len(nodeQueue)
            for i in range(level_len):
                node = nodeQueue.pop(0)
                if node.left is None and node.right is None:
                    return depth+1
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            depth+=1
        return depth
    #     return self.getMinDepth(root)
    # def getMinDepth(self, root):
    #     if root is None:
    #         return 0
    #     if root.left is None or root.right is None:
    #         return 1+max(self.getMinDepth(root.left), self.getMinDepth(root.right))
    #     else:
    #         return 1+min(self.getMinDepth(root.left), self.getMinDepth(root.right))
        
# @lc code=end

