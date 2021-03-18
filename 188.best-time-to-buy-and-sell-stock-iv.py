#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (26.73%)
# Likes:    848
# Dislikes: 56
# Total Accepted:    94.7K
# Total Submissions: 354.3K
# Testcase Example:  '2\n[2,4,1]'
#
# Say you have an array for which the i-th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
# 3.
# 
# 
#
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    # 股票 最多k次 有限次数
    # 用 dp[k][j] 表示前j天最多交易k次的最高收益，
    # 首先第 j 天可以什么都不操作，今天的最高收益就等于昨天的最高收益
    # dp[k][j] = dp[k][j-1]
    # 此外，为了获得更大收益我们第 j 天也可以选择卖出，既然选择卖出，
    # 那么在0到 j-1 天就要选择一天买入。
    # 多选择了一次买入，那在买入之前已经进行了 k-1 次买卖。
    # 在第 0 天买入，收益就是 prices[j] - prices[0] + dp[k-1][0]
    # 在第 1 天买入，收益就是 prices[j] - prices[1] + dp[k-1][1]，
    # 多加了前一天的最大收益
    # 在第 2 天买入，收益就是 prices[j] - prices[2] + dp[k-1][2]，
    # 多加了前一天的最大收益
    # ...
    # 在第 j-1 天买入，收益就是 prices[j] - prices[j-1] + dp[k-1][j-1]，
    # 多加了前一天的最大收益
    # 在第 j 天买入 prices[j] - prices[j] + dp[k-1][j]
    # localMax is max(array of kp[k-1][a]-prices[a]) a=0,1,2....j 

        length = len(prices)
        if k == 0 or length == 0:
            return 0
        if k >= length//2:
            return self.max_nolimit(prices)
        else:
            dp = [[0 for j in range(length)] for i in range(2)]
            for i in range(1, k+1):
                localMax = dp[(i-1)%2][0]-prices[0]
                for j in range(1, length):
                    localMax = max(localMax, dp[(i-1)%2][j]-prices[j])
                    dp[i%2][j] = max(dp[i%2][j-1], prices[j]+localMax)
            return max(dp[0][-1], dp[1][-1])

    def max_nolimit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit+=(prices[i]-prices[i-1])
        return profit
            

