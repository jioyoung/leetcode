#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.77%)
# Likes:    1100
# Dislikes: 82
# Total Accepted:    348.4K
# Total Submissions: 761.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort, iteration and then two pointer
        nums.sort()
        res = sum(nums[0:3])
        min_diff = abs(sum(nums[0:3]) - target)
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                diff = abs(threeSum - target)
                if threeSum == target:
                    return threeSum
                if diff < min_diff:
                    res = threeSum
                    min_diff = diff
                if threeSum > target:
                    right-=1
                else:
                    left+=1
        return res

