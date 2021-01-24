#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.39%)
# Likes:    1128
# Dislikes: 170
# Total Accepted:    308.8K
# Total Submissions: 711.5K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 寻找扭曲数组 扭曲 最小值 rotate 旋转 
        left, right = 0, len(nums)-1
        if nums[left] <= nums[right]:
            return nums[left] # do not forget this condition
        while left < right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid # right is mid not mid-1
        return nums[left]
