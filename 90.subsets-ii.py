#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (43.20%)
# Likes:    994
# Dislikes: 50
# Total Accepted:    215.8K
# Total Submissions: 499.2K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.getSubsetWithDup(nums, res, [], 0)
        return res
        
    def getSubsetWithDup(self, nums, res, rec_res, start):
        res.append(list(rec_res))
        for i in range(start, len(nums)):
            if i > start and nums[i]==nums[i-1]:
                continue
            else:
                rec_res.append(nums[i])
                self.getSubsetWithDup(nums, res, rec_res, i+1)
                rec_res.pop()
        return 
