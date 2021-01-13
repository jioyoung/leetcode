#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (57.65%)
# Likes:    2469
# Dislikes: 79
# Total Accepted:    441.8K
# Total Submissions: 766.3K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # Method 2 # backtracking
    # 排列 没有重复
        res = []
        self.getPermute(nums, res, [], len(nums))
        return res



    def getPermute(self, nums, res, res_rec, len_nums):
        if len_nums == len(res_rec):
            res.append(list(res_rec))
            return
        for i in range(len_nums):
            if nums[i] in res_rec:
                continue
            res_rec.append(nums[i])
            self.getPermute(nums, res, res_rec, len_nums)
            res_rec.pop()
        return

    # method 1: recursive swap
    # https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
    #     result = []
    #     self.generate(nums, 0, result)
    #     return result
    
    # def generate(self, nums, begin, result):
    #     if begin == len(nums):
    #         result.append(list(nums))
    #     for i in range(begin, len(nums)):
    #         nums[begin], nums[i] = nums[i], nums[begin]
    #         self.generate(nums, begin+1, result)
    #         nums[begin], nums[i] = nums[i], nums[begin]


# @lc code=end

