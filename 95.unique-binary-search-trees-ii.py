#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (37.10%)
# Likes:    1507
# Dislikes: 127
# Total Accepted:    155.2K
# Total Submissions: 417.2K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    ''' Solution 1 
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """ 
        res = []
        if n == 0:
            return res
        dp = [None]*(n+1)
        dp[0] = []
        dp[0].append(None)
        for i in range(1, n+1):
            dp[i]=[]
            for root in range(1, i+1):
                n_left = root-1
                n_right = i-root
                for left_tree in dp[n_left]:
                    for right_tree in dp[n_right]:
                        treeroot = TreeNode(root)
                        treeroot.left = left_tree
                        treeroot.right = self.clone(right_tree, root)
                        dp[i].append(treeroot)
        
        return dp[n]

    def clone(self, node, diff):
        if node is None:
            return None
        newnode = TreeNode(node.val + diff)
        newnode.left = self.clone(node.left, diff)
        newnode.right = self.clone(node.right, diff)
        return newnode
    '''

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """ 
        res = []
        if n == 0:
            return res
        return self.getRes(1, n)

    def getRes(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        
        if start==end:
            treenode = TreeNode(start)
            res.append(treenode)
            return res

        for i in range(start, end+1):
            lefttrees = self.getRes(start, i-1)
            righttrees = self.getRes(i+1, end)
            for left in lefttrees:
                for right in righttrees:
                    treenode = TreeNode(i)
                    treenode.left = left
                    treenode.right = right
                    res.append(treenode)

        return res

        
# @lc code=end

