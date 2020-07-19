#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.85%)
# Likes:    1778
# Dislikes: 91
# Total Accepted:    324.6K
# Total Submissions: 957.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 找左边界 相等也要 right = mid-1 最后左边界是有效的left
        # 找右边界 相等也要往右 left = mid+1 最后右边界是right
        
        left, right = 0, len(nums)-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        left_margin = left
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return [left_margin, right]
        
        
        #left, right = 0, len(nums)-1
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid]<target:
        #         left = mid+1
        #     else:
        #         right = mid-1
        # # 是否有效
        # if left == len(nums) or nums[left]!=target:
        #     return [-1, -1]
        # right = len(nums)-1
        # res = [None]*2
        # res[0] = left
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid]>target:
        #         right = mid-1
        #     else:
        #         left = mid +1
        # res[1]=right
        # return res

    
