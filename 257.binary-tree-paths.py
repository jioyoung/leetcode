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
        #分层 树 路径
        if not root:
            return []
        nodeQueue = [root]
        pathQueue = [[str(root.val)]]
        #yazzha each element in the pathQueue is a list: [['1', '2']... ]
        res = []
        while nodeQueue:
            length = len(nodeQueue)
            for _ in range(length):
                node = nodeQueue.pop(0)
                path = pathQueue.pop(0)
                if node.left:
                    nodeQueue.append(node.left)
                    pathQueue.append(path+[str(node.left.val)])
                if node.right:
                    nodeQueue.append(node.right) # yazzha append node not node.val
                    pathQueue.append(path+[str(node.right.val)])
                if not node.left and not node.right:
                    res.append('->'.join(path))                     
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

