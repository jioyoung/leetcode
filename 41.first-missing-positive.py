#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (29.28%)
# Likes:    1866
# Dislikes: 616
# Total Accepted:    228.5K
# Total Submissions: 778K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # if nums[i] > 0 and <= len(nums) nums[i] should be equal to i+1
        length = len(nums)
        for i in range(length):
            while 0 < nums[i]<= length and nums[i]!=nums[nums[i]-1]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
        for i in range(length):
            if nums[i]!=i+1:
                return i+1
        return length + 1 

        # length = len(nums)
        # for i in range(length):
        #     # zy: nums[i]!=nums[nums[i]-1]
        #     while 0 < nums[i]<= length and nums[i]!=nums[nums[i]-1]:
        #         temp = nums[i] - 1
        #         nums[i], nums[temp] = nums[temp], nums[i]
        
        # for i in range(length):
        #     if nums[i] != i+1:
        #         return i+1
        # return length+1

