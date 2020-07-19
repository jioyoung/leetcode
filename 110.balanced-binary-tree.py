#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.79%)
# Likes:    1493
# Dislikes: 135
# Total Accepted:    362.7K
# Total Submissions: 866.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        '''
        count_left = self.maxDepth(root.left)
        count_right = self.maxDepth(root.right)
        if abs(count_left-count_right)>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right) 
        '''
        return self.getDepth(root)!=-1

    def getDepth(self, root):
        if root is None:
            return 0
        left_depth = self.getDepth(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.getDepth(root.right)    
        if right_depth == -1:
            return -1
        if abs(left_depth-right_depth) > 1:
            return -1
        return max(left_depth, right_depth)+1


    def maxDepth(self, root):
        if not root:
            return 0
        count = 0
        queue = []
        queue.append(root)
        while queue:
            level_num = len(queue)
            for i in range(level_num):
                node = queue.pop(0)
                if node is not None:
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            count+=1
        return count


        
# @lc code=end

