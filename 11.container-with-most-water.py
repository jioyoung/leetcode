#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (44.61%)
# Likes:    3263
# Dislikes: 437
# Total Accepted:    373.6K
# Total Submissions: 837.5K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # move the lower pointer until the two pointers meet

        value = 0
        maxArea = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                value = (right-left)*height[left]
                maxArea = max(maxArea, value)
                left+=1
            else:
                value = (right-left)*height[right]
                maxArea = max(maxArea, value)
                right-=1
        return maxArea

        # res, max_res = 0, 0

        # left, right = 0, len(height)-1
        # while left < right:
        #     if height[left] < height[right]:
        #         res = height[left]*(right-left)
        #         max_res = max(res, max_res)
        #         left+=1
        #     else:
        #         res = height[right]*(right-left)
        #         max_res = max(res, max_res)
        #         right-=1
        # return max_res                


