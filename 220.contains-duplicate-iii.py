#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.70%)
# Likes:    975
# Dislikes: 1022
# Total Accepted:    118.6K
# Total Submissions: 572.9K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # seperate the num into different bucket
        if t< 0:
            return False
        width = t+1
        num_dict = dict()
        for i in range(len(nums)):
            value = nums[i]//width
            if value in num_dict:
                return True
            if (value-1) in num_dict and abs(num_dict[value-1]-nums[i])<width:
                return True
            if (value+1) in num_dict and abs(num_dict[value+1]-nums[i])<width:
                return True
            num_dict[value] = nums[i]
            if i >=k:
                del num_dict[nums[i-k]//width]
        return False
        
# @lc code=end

