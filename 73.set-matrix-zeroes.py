#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (40.48%)
# Likes:    1176
# Dislikes: 207
# Total Accepted:    225K
# Total Submissions: 556K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)
        if nrow == 0:
            return
        ncol = len(matrix[0])
        if ncol == 0:
            return
        c1_zero, r1_zero = 0, 0
        for i in range(nrow):
            if matrix[i][0] == 0:
                c1_zero = 1
                break
        for j in range(ncol):
            if matrix[0][j] == 0:
                r1_zero = 1
                break

        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1, nrow):
            for j in range(1, ncol):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        if c1_zero == 1:
            for i in range(nrow):
                matrix[i][0]=0
        if r1_zero == 1:
            matrix[0] = [0]*ncol
        





        

