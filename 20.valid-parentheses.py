#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.04%)
# Likes:    3366
# Dislikes: 156
# Total Accepted:    699.1K
# Total Submissions: 1.9M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {')':'(', ']':'[', '}':'{'}
        arr = []
        for c in s:
            if c in table:
                if not arr:
                    return False
                if arr.pop()!=table[c]:
                    return False
            else:
                arr.append(c)
        return (not arr) 



        # table = {')':'(', ']':'[', '}':'{'}
        # arr = []
        # for char in s:
        #     if char in table:
        #         if not arr:
        #             return False
        #         else:
        #             if arr.pop()!=table[char]:
        #                 return False
        #     else:
        #         arr.append(char)
        # return (not arr)
