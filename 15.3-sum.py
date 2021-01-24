#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (24.02%)
# Likes:    3783
# Dislikes: 425
# Total Accepted:    553.3K
# Total Submissions: 2.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 3sum 3 sum three sum
        # sort, iteration and two pointers
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum > -nums[i]:
                    right -=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif twoSum < -nums[i]:
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return res


