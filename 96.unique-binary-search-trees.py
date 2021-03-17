#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (47.90%)
# Likes:    2101
# Dislikes: 82
# Total Accepted:    225K
# Total Submissions: 468.1K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
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
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BST 数量 binary search tree 构建 BST
        # dp[i] 表示 节点个数为i的bst数量
        if n== 0:
            return 0
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for root in range(1, i+1):
                n_left = root-1
                n_right = i - root
                dp[i]+=dp[n_left]*dp[n_right]
        return dp[n]

# 数字个数是 0 的所有解
# null
# 数字个数是 1 的所有解
# 1
# 2
# 3
# 数字个数是 2 的所有解，我们只需要考虑连续数字
# [ 1 2 ]
#   1  
#    \    
#     2
#    2
#   /
#  1

# [ 2 3 ]
#   2  
#    \    
#     3
#    3
#   /
#  2
# 如果求 3 个数字的所有情况。
# [ 1 2 3 ]
# 利用解法二递归的思路，就是分别把每个数字作为根节点，然后考虑左子树和右子树的可能
# 1 作为根节点，左子树是 [] 的所有可能，右子树是 [ 2 3 ] 的所有可能，利用之前求出的结果进行组合。
#     1
#   /   \
# null   2
#         \
#          3

#     1
#   /   \
# null   3
#       /
#      2 

# 2 作为根节点，左子树是 [ 1 ] 的所有可能，右子树是  [ 3 ] 的所有可能，利用之前求出的结果进行组合。
#     2
#   /   \
#  1     3

# 3 作为根节点，左子树是 [ 1 2 ] 的所有可能，右子树是 [] 的所有可能，利用之前求出的结果进行组合。
#      3
#    /   \
#   1   null
#    \
#     2

#       3
#     /   \
#    2   null 
#   /
#  1

# @lc code=end

