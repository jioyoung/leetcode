#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.16%)
# Likes:    783
# Dislikes: 3787
# Total Accepted:    217.4K
# Total Submissions: 1.3M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # every time multiply temporary divisor by two
        # if dividend < divisor, set temporary divisor to be the original one
        
        if dividend == 0:
            return 0
        isNegative = not ( (dividend <0) == (divisor <0))
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >=divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                res+=i
                dividend -= temp
                temp<<=1
                i<<=1
        if isNegative:
            res = -res
        limit = 2**31
        return min(max(-limit, res), limit-1)

        
        
        
        # if dividend == 0:
        #     return 0
        # isPositive = (dividend < 0) == (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # res = 0
        # while dividend >= divisor:
        #     temp = divisor
        #     i = 1
        #     while dividend >= temp:
        #         dividend -= temp
        #         res+=i
        #         i<<=1 # x <<=y : x = x*2^y zy: <<= update i
        #         temp<<=1
        # if not isPositive:
        #     res = -res
        # return min(max(-2147483648,res), 2147483647)

