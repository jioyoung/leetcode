#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        return self.getPath(root, sum, 0) + self.pathSum(root.left, sum) + \
            self.pathSum(root.right, sum)

    def getPath(self, root, s, pre):
        if root is None:
            return 0
        cur = pre + root.val
        return (cur == s) + self.getPath(root.left, s, cur) + \
            self.getPath(root.right, s, cur)
        
# @lc code=end

