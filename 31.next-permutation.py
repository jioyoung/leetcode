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
        # 下一个 排列
        # from the end of the list, find the first value that is less than the one before it
        # 1 2 3 6 5 1 will have a result: 1 2 5 6 3 1; this is wrong
        # the reason is that 1 2 5 1 3 6 is the smallest one that is greater than the original number
        # so after exchange 5 and 3 we need to reverse the numbers after the corresponding index

        i = len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]:
            i-=1
        if i == 0:
            nums.reverse()
            return
        i-=1
        j = len(nums)-1
        while nums[j]<=nums[i]:
            j-=1
            # this loop will always terminate 
            # since nums[i+1] > nums[i]
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return 
        

