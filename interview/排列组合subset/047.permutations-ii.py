#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (42.35%)
# Likes:    1267
# Dislikes: 46
# Total Accepted:    276K
# Total Submissions: 651.5K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort nums  
        nums.sort()
        res = []
        self.getPermuteUnique(nums, res, [], [])
        return res
        
    def getPermuteUnique(self, nums, res, rec_res, rec_index):
        if len(rec_res) == len(nums):
            res.append(list(rec_res))
            return
        
        for i in range(len(nums)):
            if i in rec_index:
                continue
            if i > 0 and i-1 not in rec_index and nums[i] == nums[i-1]:
                continue
            rec_res.append(nums[i])
            rec_index.append(i)
            self.getPermuteUnique(nums, res, rec_res, rec_index)
            rec_res.pop()
            rec_index.pop()
        return

    #     res = []
    #     self.getPer(nums, res, 0)
    #     return res

    # def getPer(self, nums, res, begin):
    #     if begin == len(nums):
    #         res.append(list(nums))
    #     visit = set()
    #     for i in range(begin, len(nums)):
    #         if nums[i] in visit:
    #             continue
    #         visit.add(nums[i])
    #         nums[begin], nums[i] = nums[i], nums[begin]
    #         self.getPer(nums, res, begin+1)
    #         nums[begin], nums[i] = nums[i], nums[begin]       
# @lc code=end

