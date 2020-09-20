#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_count = {}
        degree = 0
        
        for i in range(len(nums)):
            number = nums[i]
            if number not in num_count:
                num_count[number] = [i, i, 1]
            else:
                num_count[number][1] = i
                num_count[number][2] +=1
            if num_count[number][2] > degree:
                degree = num_count[number][2]

        minLen = len(nums)
        for number in nums:
            if num_count[number][2] == degree:
                minLen = min(minLen, num_count[number][1] - num_count[number][0]+1)

        return minLen

        
# @lc code=end

