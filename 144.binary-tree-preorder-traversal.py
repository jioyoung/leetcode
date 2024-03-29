#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (52.69%)
# Likes:    1149
# Dislikes: 49
# Total Accepted:    426.9K
# Total Submissions: 793.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        preorder: root left right
        '''
        # 前序遍历 
        res = []
        nodeStack = [root]
        while nodeStack:
            node = nodeStack.pop()
            if not node:
                continue
            res.append(node.val)
            nodeStack.append(node.right)
            nodeStack.append(node.left)
        return res


    #     ret = []
    #     self.preorderHelp(root, ret)
    #     return ret

    # def preorderHelp(self, root, retList):
    #     if root is None:
    #         return
    #     retList.append(root.val)
    #     self.preorderHelp(root.left, retList)
    #     self.preorderHelp(root.right, retList)
        

# @lc code=end

