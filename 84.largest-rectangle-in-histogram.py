#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (31.84%)
# Likes:    2144
# Dislikes: 58
# Total Accepted:    187.5K
# Total Submissions: 589K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i, length = 0, len(heights)
        area = 0
        while i <= length:
            if (not stack) or (i<length and heights[i]>heights[stack[-1]]):
                stack.append(i)
                i+=1
            else:
                last=stack.pop()
                if not stack:
                    width = i
                else:
                    width = i-stack[-1]-1
                area = max(area, width*heights[last])
        return area
    
