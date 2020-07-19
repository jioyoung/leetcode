#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        n_row = len(obstacleGrid)
        n_col = len(obstacleGrid[0])
        if n_col == 1 or n_row == 1:
            total_s = sum([sum(oneList) for oneList in zip(*obstacleGrid)])    
            if total_s > 0:
                return 0
            else:
                return 1
        first_row = [1]*(n_col)
        for i in range(n_col):
            if obstacleGrid[0][i]==1:
                first_row[i:] = [0]*(n_col-i)
                break
        step_dp = [1]*(n_row)
        for i in range(n_row):
            if obstacleGrid[i][0] ==1:
                step_dp[i:] = [0]*(n_row-i)
        for j in range(1, n_col):
            for i in range(1, n_row):
                if obstacleGrid[i][j]==1:
                    step_dp[i] = 0
                else:
                    if i == 1:
                        step_dp[i] += first_row[j]
                    else:
                        step_dp[i] += step_dp[i-1]
        return step_dp[-1]
        # n_row = len(obstacleGrid)
        # n_col = len(obstacleGrid[0])
        # if obstacleGrid[0][0]==1:
        #     return 0
        # if n_row==1 or n_col ==1:
        #     for i in range(n_row):
        #         for j in range(n_col):
        #             if obstacleGrid[i][j]==1:
        #                 return 0
        #     return 1
        # matrix = [None]*n_row
        # for i in range(n_row):
        #     matrix[i]=[1]*n_col
        # for i in range(n_col):
        #     if obstacleGrid[0][i]==1:
        #         matrix[0][i:n_col] = [0]*(n_col-i)
        #         break
        # for i in range(n_row):
        #     if obstacleGrid[i][0]==1:
        #         for j in range(i,n_row):
        #             matrix[j][0]=0
        #         break
        # for i in range(1, n_row):
        #     for j in range(1, n_col):
        #         if obstacleGrid[i][j]==1:
        #             matrix[i][j]=0
        #         else:
        #             matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
        # return matrix[n_row-1][n_col-1]

