#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # sort the array based on a scheme
        # bubble sort with flag
        for i in range(len(nums)):
           nums[i] = str(nums[i])
        
        end = len(nums)
        while end:
            oldEnd = end
            end = 0
            for i in range(1, oldEnd):
                if self.compareTwoString(nums[i-1], nums[i]):
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    end = i
        if int(nums[0]) == 0:
            return '0'
        return ''.join(nums)


    def compareTwoString(self, s1, s2):
        if s1 + s2 < s2 + s1:
            return 1
        else:
            return 0

# @lc code=end

