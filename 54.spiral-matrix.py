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
        if not matrix:
            return []
        r_low, r_high = 0, len(matrix)-1
        c_low, c_high = 0, len(matrix[0])-1
        size = len(matrix)*len(matrix[0])
        direct = 0
        while (len(result)<size):
            if direct == 0:
                # right
                result = result + matrix[r_low][c_low:c_high+1]
                r_low+=1
                direct = 1
            elif direct == 1:
                # down
                for i in range(r_low, r_high+1):
                    result.append(matrix[i][c_high])
                c_high-=1
                direct =2
            elif direct ==2:
                result = result + matrix[r_high][c_low:c_high+1][::-1]
                #left
                r_high-=1
                direct = 3
            else:
                for i in range(r_high, r_low-1, -1):
                    result.append(matrix[i][c_low])
                c_low+=1
                direct = 0
        return result
