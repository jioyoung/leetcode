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
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            if sum(nums[i:i+4])> target:
                break
            target_3 = target - nums[i]
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if sum(nums[j:j+3])>target_3:
                    break
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] < target_3 - nums[j]:
                        left+=1
                    elif nums[left]+nums[right] > target_3 - nums[j]:
                        right-=1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1   
        return result

        # nums.sort()
        # result = []
        # for i in range (len(nums)-3):
        #     if i > 0 and nums[i]==nums[i-1]:
        #         continue
        #     if (nums[i]+nums[i+1]+nums[i+2]+nums[i+3]) > target:
        #         return result
        #     for j in range(i+1, len(nums)-2):
        #         if j > i+1 and nums[j]==nums[j-1]:
        #             continue
        #         k,l = j+1, len(nums)-1
        #         sum_target = target - nums[i] - nums[j]
        #         while k < l:
        #             sum = nums[k] + nums[l]
        #             if sum == sum_target:
        #                 result.append([nums[i],nums[j],nums[k],nums[l]])
        #             if sum < sum_target:
        #                 k += 1
        #                 while k < l and nums[k] == nums[k-1]:
        #                     k += 1
        #             else:
        #                 l -= 1
        #                 while k < l and nums[l] == nums[l+1]:
        #                     l -= 1
        # return result

                

        

