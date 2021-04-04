#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # rest sell buy
        # owe, notOwe
        # owe[i] = max(owe[i-1], notOwe[i-2]-price[i])
        # notOwe[i] = max(notOwe[i-1], owe[i-1]+price[i])
        if len(prices) <= 1:
            # check if the length is less than or equal to 1
            return 0
        owe = [0 for i in range(len(prices))]
        notOwe = [0 for i in range(len(prices))]
        owe[0] = -prices[0]
        owe[1] = max(-prices[0], -prices[1])
        for i in range(1, len(prices)):
            notOwe[i] = max(notOwe[i-1], owe[i-1]+prices[i])
            if i == 1:
                continue
            owe[i] = max(owe[i-1], notOwe[i-2] - prices[i])
        return notOwe[-1]


# @lc code=end

