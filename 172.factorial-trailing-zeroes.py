#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.62%)
# Likes:    594
# Dislikes: 847
# Total Accepted:    179.3K
# Total Submissions: 476.1K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#

# @lc code=start

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        分解multiplier就是看有几个5 一个5 就有一个零 2的个数肯定比5多很多 只要考虑5
        """
        count = 0
        while n > 0:
            count += (n//5)
            n = n//5
        return count
        
# @lc code=end

