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
        
# @lc code=end

