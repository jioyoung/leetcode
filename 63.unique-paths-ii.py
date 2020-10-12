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

'''
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
        
        first_row = [0]*nCol
        for i in range(nCol):
            if obstacleGrid[0][i] == 0:
                first_row[i] = 1
            else:
                break
        dp_row = [0]*nRow
        for i in range(nRow):
            if obstacleGrid[i][0] == 0:
                dp_row[i] = 1
            else:
                break
        
        for j in range(1, nCol):
            for i in range(1, nRow):
                if obstacleGrid[i][j] == 1:
                    dp_row[i] = 0
                else:
                    if i == 1:
                        dp_row[i]+=first_row[j]
                    else:
                        dp_row[i]+=dp_row[i-1]
        return dp_row[-1]
'''
                    
