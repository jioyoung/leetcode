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
        res = []
        path = []
        nums.sort()
        self.getres(nums, len(nums), 0, path, res)
        return res

    def getres(self, nums, length, index, path, res):
        res.append(path)
        for i in range(index, length):
            if i>index and nums[i]==nums[i-1]:
                continue
            self.getres(nums, length, i+1, path+[nums[i]], res)

