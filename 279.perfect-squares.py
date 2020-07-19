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
        # BFS
        num_map = dict()
        return self.getCount(n, num_map)
    
    def getCount(self, n, num_map):
        if n in num_map:
            return num_map[n]
        if n == 0:
            return 0
        i = 1
        count = n
        while i*i<=n:
            count = min(count, self.getCount(n-i*i, num_map)+1)
            i+=1
        num_map[n] = count
        return count
# @lc code=end

