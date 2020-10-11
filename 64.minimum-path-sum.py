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
        if nRow == 0:
            return 0
        nCol = len(grid[0])
        if nCol == 0:
            return 0
        for j in range(1, nCol):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,nRow):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,nRow):
            for j in range(1, nCol):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]


