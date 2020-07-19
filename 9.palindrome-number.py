#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (44.43%)
# Likes:    1628
# Dislikes: 1378
# Total Accepted:    679K
# Total Submissions: 1.5M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # get the reverse and then compare
        true_value = x
        if x < 0:
            return False
        reverse = 0
        while x:
            reverse = 10*reverse+x%10
            x = x//10
        if reverse == true_value:
            return True
        else:
            return False


        # origin_x = x
        # reverse = 0
        # if x<0:
        #     return False
        # else:
        #     while x:
        #         reverse = 10*reverse+x%10
        #         x=x//10
        # if reverse == origin_x:
        #     return True
        # else:
        #     return False
        

