#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (58.66%)
# Likes:    2009
# Dislikes: 90
# Total Accepted:    540.4K
# Total Submissions: 919.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        res = []
        stacklist = []
        cur = root
        while cur or stacklist:
            while cur:
                stacklist.append(cur)
                cur = cur.left
            cur = stacklist.pop()
            res.append(cur.val)
            cur=cur.right
        return res
        '''
        res = []
        self.getRes(root, res)
        return res
    
    def getRes(self, node, res):
        if not node:
            return
        self.getRes(node.left,res)
        res.append(node.val)
        self.getRes(node.right, res)
# @lc code=end

