#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount+1] * (amount+1)
        dp[0]=0
        for i in range(1, amount+1):
            for coinValue in coins:
                if i >= coinValue:
                    dp[i] = min(dp[i], dp[i-coinValue]+1)
        return dp[-1] if dp[-1] < amount+1 else -1
       
# @lc code=end

