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
        if not root:
            return 0
        queue = []
        count = 0
        queue.append(root)
        while queue:
            level_num = len(queue)
            for i in range(level_num):
                node = queue.pop(0)
                left_none = 0
                right_none = 0
                if node.left is not None:
                    queue.append(node.left)
                else:
                    left_none = 1
                if node.right is not None:
                    queue.append(node.right)
                else:
                    right_none = 1
                if left_none*right_none==1:
                    return count+1
            count+=1            
        
# @lc code=end

