#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (55.99%)
# Likes:    1361
# Dislikes: 135
# Total Accepted:    536K
# Total Submissions: 956.1K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        sDict = {}
        for c in s:
            if c in sDict:
                sDict[c]+=1
            else:
                sDict[c]=1
        
        for c in t:
            value = sDict.get(c, 0)
            if value == 0:
                return False
            else:
                sDict[c]-=1     
        return True
        
# @lc code=end

