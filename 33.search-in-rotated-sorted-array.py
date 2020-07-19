#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.02%)
# Likes:    2666
# Dislikes: 336
# Total Accepted:    446.9K
# Total Submissions: 1.4M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # get the mid num. judge if target is in the sorted part
        # if in, drop the other part
        # if not in, drop this part
        
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # left half is sorted
                if nums[left]<=target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right half is sorted
                if nums[mid] < target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return -1

        
        
        
        
        
        
        
        # left = 0
        # right = len(nums)-1
        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
        #     #left is sorted
        #     if nums[left]<=nums[mid]:
        #         #target in this part
        #         if nums[left]<=target and nums[mid]>target:
        #             right = mid-1
        #         else:
        #             left = mid+1
        #     else: # right is sorted
        #         if nums[mid] < target and nums[right]>=target:
        #             left = mid+1
        #         else:
        #             right = mid-1
        # return -1




        

