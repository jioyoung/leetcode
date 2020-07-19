#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (37.11%)
# Likes:    2762
# Dislikes: 71
# Total Accepted:    246.7K
# Total Submissions: 664.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dynamic programming
        # if max_edge[i][j]==1:
        # max_edge[i][j] = min(max_edge[i-1][j-1],max_edge[i-1][j],max_edge[i][j-1]) + 1
        nRow = len(matrix)
        if nRow == 0:
            return 0
        nCol = len(matrix[0])
        if nRow == 1:
            for i in range(nCol):
                if matrix[0][i] == '1':
                    return 1
            return 0
        if nCol == 1:
            for i in range(nRow):
                if matrix[i][0] == '1':
                    return 1
            return 0
        pre_top_left = 0
        max_edge = 0
        row_dp = [0]*(nCol+1)
        for i in range(1, nRow+1):
            for j in range(1, nCol+1):
                temp = row_dp[j]
                if matrix[i-1][j-1]=='0':
                    row_dp[j] = 0
                else:
                    row_dp[j] = min(row_dp[j-1], row_dp[j], pre_top_left) + 1
                    max_edge = max(max_edge, row_dp[j])
                pre_top_left = temp
        return max_edge**2

# @lc code=end

