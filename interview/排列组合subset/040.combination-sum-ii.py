#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (42.48%)
# Likes:    944
# Dislikes: 49
# Total Accepted:    235.9K
# Total Submissions: 553.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.getCombination(candidates,res, [], target, 0)
        return res
        
    def getCombination(self, candidates, res, rec_res, target, start):
        if target == 0:
            res.append(list(rec_res))
            return 
        if target < 0:
            return 
        for i in range(start, len(candidates)):
            if i > start and candidates[i-1] == candidates[i]:
                continue
            rec_res.append(candidates[i])
            self.getCombination(candidates,res, rec_res, target-candidates[i], i+1) 
            rec_res.pop()
        return

 