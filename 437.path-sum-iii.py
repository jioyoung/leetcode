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
        if not root:
            return 0
        return self.getCount(root, sum, 0) + self.pathSum(root.left, sum) + \
            self.pathSum(root.right, sum)
        
    def getCount(self, root, target, preSum):
        if not root:
            return 0
        cur = preSum + root.val
        return (cur == target) + self.getCount(root.left, target, cur) + \
            self.getCount(root.right, target, cur)

    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     return self.getPath(root, sum, [sum])

    # def getPath(self, root, origin, targets):
    #     if not root:
    #         return 0
    #     hit = 0
    #     for t in targets:
    #         if t == root.val:
    #             hit+=1
    #     targets = [value - root.val for value in targets] + [origin]
    #     return hit + self.getPath(root.left, origin, targets) + \
    #         self.getPath(root.right, origin, targets)
# @lc code=end

