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

        if not root:
            return []
        nodeQueue = [root]
        path = [[str(root.val)]]
        res = []
        while nodeQueue:
            level_len = len(nodeQueue)
            for i in range(level_len):
                node = nodeQueue.pop(0)
                pathNode = path.pop(0)
                if node.left:
                    nodeQueue.append(node.left)
                    path.append(pathNode+[str(node.left.val)])
                if node.right:
                    nodeQueue.append(node.right)
                    path.append(pathNode+[str(node.right.val)])
                if node.left is None and node.right is None:
                    res.append("->".join(pathNode))
        return res

    #     result = []
    #     if root is None:
    #         return result
    #     temp = ''
    #     self.getPaths(root, temp, result)
    #     return result
    
    # def getPaths(self, root, temp, result):
    #     if root.left is None and root.right is None:
    #         result.append(temp + str(root.val))
    #         return

    #     if root.left:
    #         self.getPaths(root.left, temp+ (str(root.val) + '->'), result)
        
    #     if root.right:
    #         self.getPaths(root.right, temp + str(root.val) + '->', result)

# @lc code=end

