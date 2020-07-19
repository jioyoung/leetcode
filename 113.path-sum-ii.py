#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (42.35%)
# Likes:    1111
# Dislikes: 41
# Total Accepted:    262.5K
# Total Submissions: 616.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        queueS = [root.val]
        visit = [[root.val]]
        while queue:
            level_n = len(queue)
            for i in range(level_n):
                node=queue.pop(0)
                currentS = queueS.pop(0)
                temp = visit.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                    queueS.append(node.left.val + currentS)
                    visit.append(temp+[node.left.val])
                if node.right is not None:
                    queue.append(node.right)
                    queueS.append(node.right.val + currentS)
                    visit.append(temp+[node.right.val])
                    continue
                if node.left is None and node.right is None and currentS == sum:
                    res.append(temp)
        return res

# @lc code=end

