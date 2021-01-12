#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n):
        matrix = [[None for j in range(n)] for i in range(n)]
        value = 1
        count = n*n
        direct = 0
        rLow, rHigh = 0, n-1
        cLow, cHigh = 0, n-1
        while value <= count:
            if direct == 0:
                for j in range(cLow, cHigh+1):
                    matrix[rLow][j] = value
                    value+=1
                rLow+=1
                direct = 1
            elif direct==1:
                for i in range(rLow, rHigh+1):
                    matrix[i][cHigh] = value
                    value+=1
                cHigh-=1
                direct =2 
            elif direct == 2:
                for j in range(cHigh, cLow-1, -1):
                    matrix[rHigh][j] = value
                    value+=1
                rHigh-=1
                direct = 3
            else:
                for i in range(rHigh, rLow-1, -1):
                    matrix[i][cLow] = value
                    value+=1
                cLow+=1
                direct = 0
        return matrix








    #     matrix = [None]*n
    #     for i in range(n):
    #         matrix[i]=[None]*n  
    #     self.spiralmat(0, n-1, 0, n-1, 1, matrix)
    #     return matrix
    
    # def spiralmat(self, row_l, row_h, col_l, col_h, index, matrix):
    #     # square matrixm, so symmetric
    #     if row_l < row_h:
    #         # top: left to right
    #         for i in range(col_l, col_h+1):
    #             matrix[row_l][i] = index
    #             index+=1
    #         # right: top to bottom
    #         for i in range(row_l+1, row_h+1):
    #             matrix[i][col_h] = index
    #             index+=1
    #         # bottom: right to left
    #         # no need to check if rol_l == rol_h, square mat
    #         for i in range(col_h-1, col_l-1, -1):
    #             matrix[row_h][i] = index
    #             index+=1
    #         # right: bot to top
    #         #no need to check if col_l == col_h
    #         for i in range(row_h-1, row_l, -1):
    #             matrix[i][col_l]=index
    #             index+=1
    #         self.spiralmat(row_l+1, row_h-1, col_l+1, col_h-1, index, matrix)
    #     elif row_l==row_h:
    #         matrix[row_l][col_l] = index
    #         return
    #     else:
    #         return
