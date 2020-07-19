#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (47.96%)
# Likes:    1522
# Dislikes: 42
# Total Accepted:    248.6K
# Total Submissions: 518.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nRow = len(grid)
        nCol = len(grid[0])
        if nRow == 1 or nCol == 1:
            return sum([sum(oneList) for oneList in zip(*grid)])
        step_dp = [None] * nRow
        step_dp[0] = grid[0][0]
        for i in range(1, nRow):
            step_dp[i] = grid[i][0] + step_dp[i-1]
        for j in range(1, nCol):
            for i in range(nRow):
                if i==0:
                    step_dp[i]+=grid[i][j]
                else:
                    step_dp[i] = min(step_dp[i-1], step_dp[i])+grid[i][j]
        return step_dp[-1]


