#
# @lc app=leetcode id=85 lang=python
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (34.15%)
# Likes:    1614
# Dislikes: 53
# Total Accepted:    130.2K
# Total Submissions: 381.1K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n_r = len(matrix)
        if n_r==0:
            return 0
        n_c = len(matrix[0])
        if n_c == 0:
            return 0
        height = [0]*n_c
        maxarea = 0
        for i in range(n_r):
            for j in range(n_c):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            max_row = self.maxRactanglebyrow(height, n_c)
            maxarea = max(maxarea, max_row)
        return maxarea
    

    def maxRactanglebyrow(self, height, length):
        i = 0
        stack = []
        vol = 0
        while i <= length:
            if (not stack) or (i<length and height[i]>height[stack[-1]]):
                stack.append(i)
                i+=1
            else:
                last = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - 1 -stack[-1]
                vol = max(vol, height[last]*width)
        return vol
 