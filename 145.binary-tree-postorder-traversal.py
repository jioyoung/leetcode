#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (50.38%)
# Likes:    1340
# Dislikes: 69
# Total Accepted:    326.3K
# Total Submissions: 625.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        postorder: left right middle
        '''
        ret = []
        self.postorderHelp(root, ret)
        return ret

    def postorderHelp(self, root, retList):
        if root is None:
            return
        self.postorderHelp(root.left, retList)
        self.postorderHelp(root.right, retList)
        retList.append(root.val)
        
# @lc code=end

