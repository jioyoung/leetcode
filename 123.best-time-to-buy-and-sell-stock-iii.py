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
        length = len(prices)
        if length <= 1:
            return 0
        else:
            preprofit = [0]*length
            postprofit = [0]*length
            curmin = prices[0]
            for i in range(1,length):
                if prices[i]>curmin:
                    preprofit[i]=max(preprofit[i-1], prices[i]-curmin)
                else:
                    curmin = prices[i]
                    preprofit[i] = preprofit[i-1]
            curmax = prices[-1]
            ## record max
            ## need to find the day to buy
            for j in range(length-2,-1,-1):
                if prices[j]<curmax:
                    postprofit[j] = max(postprofit[j+1], curmax-prices[j])
                else:
                    curmax = prices[j]
                    postprofit[j]=postprofit[j+1]
            total_max = 0
            for i in range(length):
                total_max = max(total_max, preprofit[i]+postprofit[i])
                        
            return total_max

