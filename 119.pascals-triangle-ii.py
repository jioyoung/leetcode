#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (44.71%)
# Likes:    531
# Dislikes: 175
# Total Accepted:    218.3K
# Total Submissions: 488.2K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 1:
            if rowIndex == 0:
                return [1]
            else:
                return [1,1]
        ret = [1]*(1+rowIndex)
        temp = [None]*(rowIndex-1)
        for i in range(2, rowIndex+1):
            temp[0:i-1] = ret[0:i-1]
            for j in range(1, i):
                ret[j]+=temp[j-1]
        return ret


        

