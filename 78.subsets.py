#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.22%)
# Likes:    2191
# Dislikes: 54
# Total Accepted:    395.8K
# Total Submissions: 730.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 子集 所有子集 无重复
        res = []
        self.getSubsets(nums, 0, res, [])
        return res

    def getSubsets(self, nums, start, res, rec_res):
        res.append(list(rec_res))
        for i in range(start, len(nums)):
            rec_res.append(nums[i])
            self.getSubsets(nums, i+1, res, rec_res)
            rec_res.pop()
        return

