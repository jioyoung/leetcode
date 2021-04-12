#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.32%)
# Likes:    3554
# Dislikes: 118
# Total Accepted:    794.4K
# Total Submissions: 1.4M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 0 放到最后 two pointer
        i = j = 0
        # j is the pointer for the non-zero value
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        return
        # j= 0 
        # for value in nums:
        #     if value == 0:
        #         continue
        #     else:
        #         nums[j]=value
        #         j+=1
        # for i in range(j, len(nums)):
        #     nums[i]=0
        # return

        
# @lc code=end

