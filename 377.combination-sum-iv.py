#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
    # dynamic programming
    # dp[0] = 0
    # dp[i] = number of combinations to get i
    # traversal 
    # if nums[i] == n: dp[n] +=1
    # elif nums[i] <n: dp[n] += dp[n-nums[i]]
        combinationDP = [0] * (target+1)
        for n in range(1, target+1):
            for i in range(len(nums)):
                if nums[i] == n:
                    combinationDP[n] += 1
                elif nums[i] < n:
                    combinationDP[n] += combinationDP[n-nums[i]]
        return combinationDP[-1]
        
# @lc code=end

