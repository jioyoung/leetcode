#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 山峰 峰值 peak
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
    
        
        
# @lc code=end

