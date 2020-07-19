#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.66%)
# Likes:    5982
# Dislikes: 343
# Total Accepted:    1M
# Total Submissions: 3.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = maxLen = 0
        char_dict = dict()
        # start is the starting index of the substring
        # for char_dict, key is the char and the value 
        # is the latest index of the char
        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]] >= start:
                start = char_dict[s[i]]+1
            else:
                maxLen = max(maxLen, i-start+1)
            char_dict[s[i]] = i
        return maxLen




        # start = max_rest = 0
        # usedChar = {}
        # for i in range(len(s)):
        #     if s[i] in usedChar and usedChar[s[i]]>=start:
        #         start=usedChar[s[i]]+1
        #     else:
        #         max_rest = max(max_rest, i-start+1)
        #     usedChar[s[i]]=i
        # return max_rest



