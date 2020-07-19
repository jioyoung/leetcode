#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (38.29%)
# Likes:    1065
# Dislikes: 296
# Total Accepted:    257.7K
# Total Submissions: 662.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        if len(s)==0:
            return True
        nums1 = self.convert(s)
        nums2 = self.convert(t)
        if nums1 == nums2:
            return True
        else:
            return False
    
    def convert(self, strs):
        nums = []
        visit = {}
        i = 0
        for c in strs:
            if c not in visit:
                visit[c] = str(i)
                nums.append(str(i))
                i+=1
            else:
                nums.append(str(visit[c]))
        return int(''.join(nums))



        
# @lc code=end

