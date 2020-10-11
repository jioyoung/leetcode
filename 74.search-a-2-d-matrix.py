#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix, target):
        # binary search regard the matrix as an array
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        left = 0
        right = m*n-1
        while left <= right:
            mid = (left+right)//2
            # mid = iRow*n+iCol
            iRow = mid//n
            iCol = mid%n
            if matrix[iRow][iCol] == target:
                return True
            elif matrix[iRow][iCol] < target:
                left = mid+1
            else:
                right = mid-1
        return False
