#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nRow = len(obstacleGrid)
        if nRow == 0:
            return 0
        nCol = len(obstacleGrid[0])
        if nCol==0:
            return 0
        
        if obstacleGrid[0][0] ==1:
            return 0
        
        if nRow == 1 or nCol == 1:
            tot_sum = sum([sum(oneList) for oneList in obstacleGrid])
            if tot_sum > 0:
                return 0
        
        for j in range(1, nCol):
            if obstacleGrid[0][j] == 0:
                obstacleGrid[0][j] = 1
            else:
                for i in range(j, nCol):
                    obstacleGrid[0][i] = 0
                break
        
        for i in range(1, nRow):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                for j in range(i, nRow):
                    obstacleGrid[j][0] = 0
                break
        obstacleGrid[0][0] = 1
        for i in range(1, nRow):
            for j in range(1, nCol):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1])
        return obstacleGrid[-1][-1]
                    
