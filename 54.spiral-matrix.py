#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (30.97%)
# Likes:    1234
# Dislikes: 433
# Total Accepted:    251.3K
# Total Submissions: 811.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 旋转 矩阵 扭曲
        result = []
        nRow = len(matrix)
        if nRow == 0:
            return []
        nCol = len(matrix[0])
        if nCol == 0:
            return []
        size = 0
        count = nRow * nCol
        direct = 0
        lRow, uRow = 0, nRow-1
        lCol, uCol = 0, nCol-1
        while size < count:
            if direct == 0:
                # right
                result+=matrix[lRow][lCol:uCol+1]
                size+=(uCol+1-lCol)
                direct = 1
                lRow+=1
            elif direct == 1:
                # down
                for i in range(lRow, uRow+1):
                    result.append(matrix[i][uCol])
                size+=(uRow+1-lRow)
                direct=2
                uCol-=1
            elif direct ==2:
                # left
                result+=matrix[uRow][lCol:uCol+1][::-1]
                size+=(uCol+1-lCol)
                direct = 3
                uRow-=1
            else:
                #up
                for i in range(uRow, lRow-1,-1):
                    result.append(matrix[i][lCol])
                size+=(uRow+1-lRow)
                direct = 0
                lCol+=1
        return result

