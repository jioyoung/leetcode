#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (59.26%)
# Likes:    4457
# Dislikes: 388
# Total Accepted:    504.5K
# Total Submissions: 850.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # firstly get the product till i-1 and assign 
        # it to res[i]
        # then calculate right half product step by step
        # update the res simultaneously
        length = len(nums)
        res = [None]*length
        res[0] = 1
        for i in range(1, length):
            res[i] = res[i-1]*nums[i-1]
        right = 1
        for i in range(length-2, -1, -1):
            right *=nums[i+1]
            res[i] *=right
        return res
# @lc code=end

