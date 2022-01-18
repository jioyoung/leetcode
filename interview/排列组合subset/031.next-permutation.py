#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.74%)
# Likes:    1955
# Dislikes: 621
# Total Accepted:    253.3K
# Total Submissions: 823K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # from the end of the list, find the first value that is less than the one before it
        # 1 2 3 6 5 1 will have a result: 1 2 5 6 3 1; this is wrong
        # the reason is that 1 2 5 1 3 6 is the smallest one that is greater than the original number
        # so after exchange 5 and 3 we need to reverse the numbers after the corresponding index

        i = len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]:
            i-=1
        if i == 0: 
            # the original nums is descending
            return nums.reverse()
        # find the first index that is greater than i-th num
        j = len(nums) -1
        i-=1
        while nums[j]<=nums[i]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[:i:-1]
        return 
        






        
        
        # #firstly, from the last num, find the first number that is not ascending
        # i = len(nums)-1
        # while i > 0 and nums[i-1]>=nums[i]:
        #     i-=1
        # if i == 0:
        #     return nums.reverse()
        # j = len(nums)-1
        # i = i-1
        # while nums[j] <= nums[i]:
        #     j -=1
        # nums[i], nums[j] = nums[j], nums[i]
        # # reverse the part between after i so that the result num is least one that is larger than the original
        # nums[i+1:] = nums[:i:-1]

