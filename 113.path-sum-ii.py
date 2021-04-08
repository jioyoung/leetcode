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
        # 树 分层 路径 和 目标
        # if not root:
        #     return []
        # nodeQueue = [root]
        # sumQueue = [root.val]
        # visitQueue = [[root.val]]
        # res = []
        # while nodeQueue:
        #     levelLen = len(nodeQueue)
        #     for i in range(levelLen):
        #         node = nodeQueue.pop(0)
        #         currentSum = sumQueue.pop(0)
        #         tempPath = visitQueue.pop(0)
        #         if node.left:
        #             nodeQueue.append(node.left)
        #             sumQueue.append(node.left.val+currentSum)
        #             visitQueue.append(tempPath+[node.left.val])
        #         if node.right:
        #             nodeQueue.append(node.right)
        #             sumQueue.append(node.right.val+currentSum)
        #             visitQueue.append(tempPath+[node.right.val])
        #         if node.left is None and node.right is None and currentSum == sum:
        #             res.append(list(tempPath))
        # return res
        res = []
        self.getPath(root, sum, res, [])
        return res

    def getPath(self, root, target, res, rec_res):
        if not root:
            return
        if root.left is None and root.right is None:
            if root.val == target:
                res.append(rec_res+[root.val])
                return
            else:
                return
        rec_res.append(root.val)
        self.getPath(root.left, target-root.val, res, rec_res)
        rec_res.pop()

        rec_res.append(root.val)
        self.getPath(root.right, target-root.val, res, rec_res)
        rec_res.pop()
        return

# @lc code=end

