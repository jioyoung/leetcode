#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (38.78%)
# Likes:    1173
# Dislikes: 375
# Total Accepted:    360.6K
# Total Submissions: 927.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 树 分层 路径 和
        if not root:
            return False
        nodeQueue= [root]
        sumQueue = [root.val]
        while nodeQueue:
            level_len = len(nodeQueue)
            for i in range(level_len):
                node = nodeQueue.pop(0)
                currentSum = sumQueue.pop(0)
                if node.left:
                    nodeQueue.append(node.left)
                    sumQueue.append(currentSum+node.left.val)
                if node.right:
                    nodeQueue.append(node.right)
                    sumQueue.append(currentSum+node.right.val)
                if node.left is None and node.right is None and currentSum == sum:
                    return True
        return False


        
# @lc code=end

