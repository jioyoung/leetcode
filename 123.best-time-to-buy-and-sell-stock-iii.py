#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (34.46%)
# Likes:    1266
# Dislikes: 56
# Total Accepted:    160.9K
# Total Submissions: 466.8K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 股票 两次
        # preprofit[i] 又买有卖到i最大利润
        # postprofit[i] 从i开始 买卖 最大利润
        '''
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
        # localMax is max(array of dp[k-1][a]-prices[a]) a=0,1,2....j         
        localMax = max(dp[k-1][i]-prices[i]) i=0,1,....
        dp[k][j] = max(dp[k][j-1], prices[j] + localMax)
        '''
        k = 2
        length = len(prices)
        if length <= 1 or k == 0:
            return 0
        if k >= length//2:
            return self.max_nolimit(prices)

        dp = [[0 for j in range(length)] for i in range(2)]
        for i in range(1, k+1):
            localMax = dp[(i-1)%2][0] - prices[0]
            for j in range(1, length):
                localMax = max(localMax, dp[(i-1)%2][j] - prices[j])
                dp[i%2][j] = max(localMax + prices[j], dp[i%2][j-1])
        return max(dp[0][-1], dp[1][-1])

    def max_nolimit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit+=diff
        return profit



