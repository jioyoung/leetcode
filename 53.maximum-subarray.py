#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.15%)
# Likes:    4735
# Dislikes: 176
# Total Accepted:    584.4K
# Total Submissions: 1.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # curMax is 以current element 结尾的子数组的元素的最大的和
        cur_max = all_max = nums[0]
        for i in range(1,len(nums)):
            if cur_max < 0:
                cur_max = nums[i]
            else:
                cur_max += nums[i]
            all_max = max(cur_max, all_max)
        return all_max

