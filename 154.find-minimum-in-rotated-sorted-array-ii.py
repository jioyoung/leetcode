#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (39.66%)
# Likes:    511
# Dislikes: 154
# Total Accepted:    139K
# Total Submissions: 350.5K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1        
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                # min in the right part
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right-=1
        return nums[left]

