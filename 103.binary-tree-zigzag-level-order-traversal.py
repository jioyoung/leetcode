#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (43.38%)
# Likes:    1247
# Dislikes: 72
# Total Accepted:    260.9K
# Total Submissions: 599.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        count = 0 # count is even left to right; odd, right->left
        queue = []
        queue.append(root)
        while queue:
            level_len = len(queue)
            sublist = []
            if count%2==0:
                for i in range(level_len):
                    node = queue.pop(0)
                    if node is not None:
                        queue.append(node.left)
                        queue.append(node.right)
                        sublist.append(node.val)
            else:
                for i in range(level_len):
                    node = queue.pop(0)
                    if node is not None:
                        queue.append(node.left)
                        queue.append(node.right)
                        sublist.insert(0, node.val)
            count+=1
            if sublist:
                res.append(sublist)
        return res

        
# @lc code=end

