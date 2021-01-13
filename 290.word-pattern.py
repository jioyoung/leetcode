#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.58%)
# Likes:    1005
# Dislikes: 144
# Total Accepted:    181.8K
# Total Submissions: 496.6K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_array = str.split()
        if len(pattern) != len(word_array):
            return False
        char_dict = {}
        for i in range(len(pattern)):
            c = pattern[i]
            if c in char_dict:
                if word_array[i] == char_dict[c]:
                    continue
                else:
                    return False
            else:
                if word_array[i] in char_dict.values():
                    return False
                char_dict[c] = word_array[i]
        return True

        
# @lc code=end

