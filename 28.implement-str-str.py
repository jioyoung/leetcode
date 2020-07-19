#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (32.66%)
# Likes:    1043
# Dislikes: 1495
# Total Accepted:    493.8K
# Total Submissions: 1.5M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
# 0 1 2 3 4 5
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # in python str1.find(str2) can be used
        # but this is not allowed in the algorithm test
        # result = haystack.find(needle) 
        # return result

        # if not needle:
        #     return 0
        # if len(haystack) < len(needle):
        #     return -1
        # for i in range(len(haystack)-len(needle)+1):
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j == len(needle)-1:
        #             return i
        # return -1


        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1





        # if not needle:
        #     return 0
        # lStr = len(needle)
        # lhay = len(haystack)
        # if lhay < lStr:
        #     return -1
        # for i in range(lhay-lStr+1):
        #     if haystack[i:i+lStr] == needle:
        #         return i
        # return -1

        

