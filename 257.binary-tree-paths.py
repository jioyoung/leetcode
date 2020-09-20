#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if root is None:
            return result
        temp = ''
        self.getPaths(root, temp, result)
        return result
    
    def getPaths(self, root, temp, result):
        if root.left is None and root.right is None:
            result.append(temp + str(root.val))
            return

        if root.left:
            self.getPaths(root.left, temp+ (str(root.val) + '->'), result)
        
        if root.right:
            self.getPaths(root.right, temp + str(root.val) + '->', result)
            
        

        
# @lc code=end

