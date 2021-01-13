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
        # 最大面积 用 dp[i][j] 表示以 matrix[i][j] 为右下角正方形的最大边长
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
        # 下边是空间复杂度优化的代码，最关键的是用 pre_top_left 保存了左上角的值
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

    # 代码的话，使用个技巧，那就是行和列多申请一行，这样的话第一行和第一列的情况就不需要单独考虑了。
    # int rows = matrix.length;
    # if (rows == 0) {
    #     return 0;
    # }
    # int cols = matrix[0].length;
    # int[][] dp = new int[rows + 1][cols + 1];
    # int maxSide = 0;
    # for (int i = 1; i <= rows; i++) {
    #     for (int j = 1; j <= cols; j++) {
    #         //因为多申请了一行一列，所以这里下标要减 1
    #         if (matrix[i - 1][j - 1] == '0') {
    #             dp[i][j] = 0;
    #         } else {
    #             dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
    #             maxSide = Math.max(dp[i][j], maxSide);
    #         }
    #     }
    # }
    # return maxSide * maxSide;


# @lc code=end

