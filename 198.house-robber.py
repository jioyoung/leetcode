#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.33%)
# Likes:    3384
# Dislikes: 113
# Total Accepted:    405.5K
# Total Submissions: 977.4K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
'''
动态规划 
到i th house
res[i] = max(res[i-1], res[i-2]+nums[i])
'''

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret_lag2 = 0
        ret_lag1 = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            res = max(ret_lag2+nums[i], ret_lag1)
            ret_lag2, ret_lag1 = ret_lag1, res
        return res

        
# @lc code=end

