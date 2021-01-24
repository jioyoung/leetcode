#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix, target):
        # binary search regard the matrix as an array
        # 寻找 矩阵
        nRow = len(matrix)
        if nRow == 0:
            return False
        nCol = len(matrix[0])
        if nCol == 0:
            return False
        left, right = 0, nCol*nRow-1
        while left <= right:
            mid = (left+right)//2
            iRow = mid//nCol
            iCol = mid%nCol
            if matrix[iRow][iCol]==target:
                return True
            elif matrix[iRow][iCol]>target:
                right = mid-1
            else:
                left = mid+1
        return False

