#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (37.19%)
# Likes:    769
# Dislikes: 932
# Total Accepted:    258.2K
# Total Submissions: 694.2K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if i-nums_dict[nums[i]]<=k:
                    return True
                else:
                    nums_dict[nums[i]] = i
            else:
                nums_dict[nums[i]] = i
        return False
        
# @lc code=end

