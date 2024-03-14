#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        minValue = min(nums)
        maxValue = max(nums)
        if minValue == maxValue:
            return 0
        n = len(nums)
        interval = 0
        if (maxValue - minValue) % (n-1) == 0:
            interval = (maxValue - minValue) // (n-1)
        else:
            interval = (maxValue - minValue) // (n-1) + 1
        bucket_min = (n-1) * [float('inf')]
        bucket_max = (n-1) * [-1]
        for value in nums:
            if value == minValue or value == maxValue:
                continue
            index = (value - minValue) // interval
            if value > bucket_max[index]:
                bucket_max[index] = value
            if value < bucket_min[index]:
                bucket_min[index] = value
        preMax = minValue
        res = 0
        for i in range(n-1):
            if bucket_max[i] == -1:
                continue
            res = max(res, bucket_min[i] - preMax)
            preMax = bucket_max[i]
        res = max(res, maxValue - preMax)
        return res 


# @lc code=end

