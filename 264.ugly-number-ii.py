#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (39.32%)
# Likes:    1477
# Dislikes: 89
# Total Accepted:    139.2K
# Total Submissions: 353.7K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # three pointers
        ugly=[1]
        i2, i3, i5 = 0,0,0
        while n > 1:
            factor2, factor3, factor5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            factor_min = min(factor2, factor3, factor5)
            if factor_min == factor2:
                i2+=1
            if factor_min == factor3:
                i3+=1
            if factor_min == factor5:
                i5+=1
            ugly.append(factor_min)
            n-=1
        return ugly[-1]
# @lc code=end

