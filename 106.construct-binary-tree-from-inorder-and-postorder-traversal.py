#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (40.45%)
# Likes:    968
# Dislikes: 20
# Total Accepted:    163.9K
# Total Submissions: 405.3K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 中序 后序 构建 构造 树
        root = self.getTree(inorder, postorder)
        return root

    def getTree(self, inorder, postorder):
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.getTree(inorder[index+1:], postorder)
            root.left = self.getTree(inorder[:index], postorder)
            return root
        else:
            return None
