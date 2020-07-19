#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.32%)
# Likes:    2176
# Dislikes: 213
# Total Accepted:    286.9K
# Total Submissions: 887.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # find the current maximum range and then find 
        # 0 element; if maximum is beyond the 0, then skip
        # if not return False
        # pay attention to the last element:
        # no need to let the current max be greater than last index
        # just let he current max be equal or greater than last index
        if len(nums)<=1:
            return True
        stepMax = nums[0]
        
        for i in range(len(nums)-1):
            if nums[i] == 0:
                if stepMax <= i:
                    return False
                else:
                    continue
            else:
                stepMax = max(i+nums[i], stepMax)
        if stepMax >= len(nums)-1:
            return True
        else:
            return False


