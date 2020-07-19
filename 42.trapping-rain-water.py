#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (43.84%)
# Likes:    3979
# Dislikes: 73
# Total Accepted:    318.6K
# Total Submissions: 724.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution(object):
    def trap(self, height):
        if not height or len(height) < 3:
            return 0
        '''
        left, right = 0, len(height)-1
        lmax, rmax = height[left], height[right]
        vol = 0
        while left < right:
            if lmax <= rmax:
                left += 1
                lmax = max(lmax, height[left])
                vol+=lmax-height[left]
            else:
                right -= 1
                rmax = max(rmax, height[right])
                vol+=rmax-height[right]
        return vol
        '''

        # stack  decreasing stack
        stack = []
        i = 0
        result = 0
        while i<len(height):
            if (not stack) or height[i]<=height[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                last = stack.pop()
                if not stack:
                    continue 
                result += (min(height[stack[-1]], height[i]) - height[last])*(i-stack[-1]-1)
        return result
        # stack = []
        # i = 0
        # vol=0
        # while i < len(height):
        #     if (not stack) or (height[i]<=height[stack[-1]]):
        #         stack.append(i)
        #         i+=1
        #     else:
        #         last = stack.pop()
        #         if not stack:
        #             continue
        #         vol+= (min(height[i], height[stack[-1]])-height[last])*(i-1-stack[-1]) 
        # return vol


        
