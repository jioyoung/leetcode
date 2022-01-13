#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numCount = {}
        degree = 0
        for i, value in enumerate(nums):
            if value not in numCount:
                numCount[value] = [i, i, 1]
            else:
                numCount[value][1] = i
                numCount[value][2] += 1
            if numCount[value][2] > degree:
                degree = numCount[value][2]
        minL = len(nums)
        for value in numCount:
            if numCount[value][2] == degree:
                distance = numCount[value][1] - numCount[value][0] + 1
                if distance < minL:
                    minL = distance
        return minL

        
# @lc code=end

