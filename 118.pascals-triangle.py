#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (47.29%)
# Likes:    801
# Dislikes: 80
# Total Accepted:    275.5K
# Total Submissions: 582.5K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=numRows
        if n == 0:
            return []
        if n ==1:
            return [[1]]
        if n ==2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(3, n+1):
            temp = [None]*i
            temp[0] = 1
            temp[-1] = 1
            for j in range(1, i-1):
                temp[j] = res[-1][j]+res[-1][j-1]
            res.append(temp)
        return res    

