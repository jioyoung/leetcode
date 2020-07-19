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
        length = len(prices)
        if length<=1 or k == 0:
            return 0
        else:
            if k >= (length//2):
                return self.max_nolimit(prices, length)
            else:
                dp = [None]*(2)
                for i in range(2):
                    dp[i]=[0]*length
                for i in range(1, k+1):
                    localmax = dp[(i-1)%2][0]-prices[0]
                    for j in range(1, length):
                        localmax = max(localmax, dp[(i-1)%2][j]-prices[j])
                        dp[i%2][j] = max(dp[i%2][j-1], prices[j]+localmax)

                    
                return max(dp[0][length-1], dp[1][length-1])
    
    def max_nolimit(self, prices, length):
        profit = 0
        for i in range(1, length):
            diff = prices[i]-prices[i-1]
            if prices[i]>prices[i-1]:
                profit+=diff
        return profit
            

