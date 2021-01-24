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
        # 颜色排列 012 排序
        rightZero = 0
        leftTwo = len(nums)-1
        i = 0
        while i <= leftTwo:
            if nums[i]==0:
                nums[rightZero], nums[i] = nums[i], nums[rightZero]
                rightZero+=1
                i+=1
            elif nums[i]==2:
                nums[leftTwo], nums[i] = nums[i], nums[leftTwo]
                leftTwo-=1
            else:
                i+=1
        return
    



