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
        res = []
        path = []
        self.getsubset(nums, 0, path, res)
        return res

    def getsubset(self, nums, index, path, res):
        if index == len(nums):
            res.append(list(path))
            return
        #not include nums[index]
        self.getsubset(nums, index+1, path, res)

        #include nums[index]
        path.append(nums[index])
        self.getsubset(nums, index+1, path, res)
        path.pop()




