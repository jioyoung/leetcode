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
        if len(nums)==0:
            return
        start_0 = 0
        end_2 = len(nums)-1
        i=0
        while i<=end_2:
            if nums[i]==0:
                nums[start_0], nums[i] = nums[i], nums[start_0]
                start_0+=1
                i+=1
            elif nums[i]==2:
                nums[end_2], nums[i] = nums[i], nums[end_2]
                end_2-=1
            else:
                i+=1
