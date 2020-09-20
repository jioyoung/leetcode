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
        ugly = [None] * n
        id2, id3, id5 = 0,0,0
        ugly[0] = 1
        for i in range(1, n):
            candidate2 = ugly[id2] * 2
            candidate3 = ugly[id3] * 3
            candidate5 = ugly[id5] * 5
            minVal = min(candidate2, candidate3, candidate5)
            if minVal == candidate2:
                id2+=1
            if minVal == candidate3:
                id3+=1
            if minVal == candidate5:
                id5+=1
            ugly[i] = minVal

        return ugly[-1]


# @lc code=end

