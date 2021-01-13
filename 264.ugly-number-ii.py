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
        # 丑数
        if n == 1:
            return 1
        uglyArr = [None]*n
        uglyArr[0] = 1
        idx_2, idx_3, idx_5 = 0, 0, 0
        for i in range(1, n):
            value2 = uglyArr[idx_2]*2
            value3 = uglyArr[idx_3]*3
            value5 = uglyArr[idx_5]*5
            minValue = min(value2, value3, value5)
            # 并列关系 yazzha
            if value2 == minValue:
                idx_2+=1
            if value3 == minValue:
                idx_3+=1
            if value5 ==minValue:
                idx_5+=1
            uglyArr[i] = minValue
        return uglyArr[-1]


# @lc code=end

