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
        length = len(nums)
        if nums[0]<=nums[-1]:
            return nums[0]
        else:
            left, right = 0, length-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]<nums[left]:
                    if nums[mid] < nums[mid-1]:
                        return nums[mid]
                    else:
                        right=mid-1
                else:
                    if nums[mid]>nums[mid+1]:
                        return nums[mid+1]
                    else:
                        left = mid+1


