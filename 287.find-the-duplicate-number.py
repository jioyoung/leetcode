#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (53.47%)
# Likes:    4076
# Dislikes: 506
# Total Accepted:    297.5K
# Total Submissions: 555.3K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # binary search for mid count the num that is less 
        # than or equal to mid
        # 原数组不是有序，但是我们知道重复的那个数字肯定是 1 到 n 中的某一个，
        # 而 1,2...,n 就是一个有序序列。因此我们可以对 1,2...,n 进行二分查找。
        # 一个数重复 重复
        # complexity is O(n * log(n))
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for value in nums:
                if value <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

        
# @lc code=end

