#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.98%)
# Likes:    1614
# Dislikes: 1474
# Total Accepted:    544.9K
# Total Submissions: 1.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefixL = 0
        charList = list(zip(*strs))
        for oneList in charList: 
            if len(set(oneList)) > 1:
                break
            prefixL+=1
        return strs[0][:prefixL]
        

        # if not strs:
        #     return ""
        # max_l = 0
        # different = False
        # i = 0
        # size_str = len(strs)
        # while i < len(strs[0]):
        #     char = strs[0][i]
        #     for j in range(1, size_str):
        #         if i >= len(strs[j]):
        #             different = True
        #             break
        #         if strs[j][i] != char:
        #             different = True
        #             break
        #     if different:
        #         break
        #     else:
        #         max_l +=1             
        #     i+=1
        # if max_l == 0:
        #     return ""
        # else:
        #     return strs[0][:max_l]
        
