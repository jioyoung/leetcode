#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (56.02%)
# Likes:    656
# Dislikes: 1012
# Total Accepted:    280.7K
# Total Submissions: 500.8K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        while num >=10:
            newNum = 0
            while num:
                newNum += num%10
                num = num//10
            num = newNum
        return num
        
# @lc code=end

