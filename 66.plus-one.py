#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.54%)
# Likes:    946
# Dislikes: 1668
# Total Accepted:    423.9K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # find a value that is less than or equal to 8 then done!
        for i in range(len(digits)-1, -1, -1):
            if digits[i] <= 8:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
        

