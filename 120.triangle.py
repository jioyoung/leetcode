#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (40.29%)
# Likes:    1242
# Dislikes: 139
# Total Accepted:    193.3K
# Total Submissions: 479.9K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length<=1:
            if length==0:
                return 0
            else:
                return triangle[0][0]
        else:
            for i in range(1, length):
                triangle[i][0] += triangle[i-1][0]
                for j in range(1,i):
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                triangle[i][i] +=triangle[i-1][i-1]
            return min(triangle[length-1])
