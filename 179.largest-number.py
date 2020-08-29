#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        pos = len(nums)
        while pos > 0:
            k = pos
            pos = 0
            for j in range(1, k):
                if self.compare2nums(nums[j-1], nums[j]):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    pos = j
        res = ''.join(nums)
        if res[0] == '0':
            return '0'
        else:
            return res
        

    def compare2nums(self, strNum1, strNum2):
        string1 = strNum1 + strNum2
        string2 = strNum2 + strNum1
        if string1 < string2:
            return 1
        else:
            return 0
# @lc code=end

