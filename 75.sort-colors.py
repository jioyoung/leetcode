#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right_0 = 0
        left_2 = len(nums)-1
        i = 0
        while i <= left_2:
            if nums[i]==0:
                nums[i], nums[right_0] = nums[right_0], nums[i]
                right_0+=1
                i+=1
            elif nums[i] == 2:
                nums[i], nums[left_2] = nums[left_2], nums[i]
                left_2-=1
                # do not update i, check if it is zero
            else:
                i+=1
