#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (46.12%)
# Likes:    1030
# Dislikes: 271
# Total Accepted:    269K
# Total Submissions: 576.1K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        sum = 0
        if n == 0:
            return False
        while n != 1:
            sum = 0
            while n > 0:
                num = n % 10
                n = n // 10
                sum+= (num*num)
            if sum in visit:
                return False
            else:
                visit.add(sum)
            n = sum
        return True

