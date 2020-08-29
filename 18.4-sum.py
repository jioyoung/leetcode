#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (30.95%)
# Likes:    1145
# Dislikes: 229
# Total Accepted:    245.6K
# Total Submissions: 793.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        # """

        nums.sort()
        ret = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if sum(nums[i:i+4]) > target:
                return ret
            three_target = target - nums[i]
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if sum(nums[j:j+3]) > three_target:
                    break
                left, right = j+1, len(nums)-1
                two_target = three_target - nums[j]
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum > two_target:
                        right -=1
                    elif two_sum < two_target:
                        left+=1
                    else:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        left +=1 
                        right -=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                
        return ret
                    

