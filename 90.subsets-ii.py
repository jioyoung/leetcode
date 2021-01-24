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
        # 所有子集 所有 子集 有重复
        res = []
        nums.sort()
        self.getSubsets(nums, 0, res, [])
        return res


    def getSubsets(self, nums, start, res, rec_res):
        res.append(list(rec_res))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            rec_res.append(nums[i])
            self.getSubsets(nums, i+1, res, rec_res)
            rec_res.pop()
        return

