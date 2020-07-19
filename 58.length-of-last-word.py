#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.30%)
# Likes:    448
# Dislikes: 1843
# Total Accepted:    300.9K
# Total Submissions: 931.3K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        if not s:
            return 0
        count = 0
        loc = len(s)-1
        while loc >= 0:
            if s[loc]!=' ':
                count+=1
                loc-=1
            else:
                return count
        return count

        # word_start = 0
        # count = 0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] == ' ':
        #         if not word_start:
        #             continue
        #         else:
        #             return count
        #     else:
        #         word_start=1
        #         count+=1
        # return count
        
# @lc code=end

