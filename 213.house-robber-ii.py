#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.13%)
# Likes:    1533
# Dislikes: 47
# Total Accepted:    162.3K
# Total Submissions: 449.3K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # seperate the whole array into two arrays
        # array[0: len -1] array[1:len]
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        return max(self.getMaxRobValue(0, length-2, nums), self.getMaxRobValue(1, length-1, nums))
        
    def getMaxRobValue(self, start, end, nums):
        ## start end are both inclusive
        lag2 = 0
        lag1 = res = nums[start]
        for i in range(start+1, end+1):
            res = max(lag2+nums[i], lag1)
            lag2, lag1 = lag1, res
        return res 
        
# @lc code=end

