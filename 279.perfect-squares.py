#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (45.42%)
# Likes:    2482
# Dislikes: 177
# Total Accepted:    269.6K
# Total Submissions: 592.6K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bfs 平方和 平方 完美平方数
        # O(n * sqrt(n))
        numDict = {0:0}
        return self.getRes(n, numDict)
    
    def getRes(self, n, numDict):
        if n in numDict:
            return numDict[n]
        res = n
        i = 1
        while i*i<=n:
            res = min(res, 1+self.getRes(n-i*i, numDict))
            i+=1
        numDict[n] = res
        return res


# @lc code=end

