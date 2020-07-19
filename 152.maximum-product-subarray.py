#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.77%)
# Likes:    2363
# Dislikes: 112
# Total Accepted:    230.7K
# Total Submissions: 774.6K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMin, curMax = nums[0], nums[0]
        ret = nums[0]
        for i in range(1,len(nums)):
            value = nums[i]
            temp = curMin
            curMin = min(curMin*value, curMax*value, value)
            curMax = max(temp*value, curMax*value, value)
            ret = max(ret, curMax)
        return ret
# @lc code=end

