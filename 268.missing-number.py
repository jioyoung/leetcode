#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (50.92%)
# Likes:    1581
# Dislikes: 1940
# Total Accepted:    423.9K
# Total Submissions: 832.2K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # since in the range(len(nums)) the largest one that is 
        # len(nums) is not included
        # result = len(nums)
        # for i in range(len(nums)):
        #     result = result ^ i ^ nums[i]
        # return result
        nRight = len(nums)
        true_sum = (1+nRight)*nRight/2
        return true_sum-sum(nums)
        
# @lc code=end

