#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (49.53%)
# Likes:    2199
# Dislikes: 68
# Total Accepted:    368.8K
# Total Submissions: 742.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # backtracking
        res = []
        self.getCombination(0, candidates, target, res, [])
        return res
    
    def getCombination(self, start, candidates, target, res, rec_res):
        if target == 0:
            res.append(list(rec_res))
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            rec_res.append(candidates[i])
            self.getCombination(i, candidates, target-candidates[i], res, rec_res)
            rec_res.pop()
        return

