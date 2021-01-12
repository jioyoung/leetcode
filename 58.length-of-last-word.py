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

        newS = s.rstrip()
        if not newS:
            return 0
        i = len(newS) -1 
        count = 0
        while i >= 0 and newS[i].isalpha():
            i-=1
            count+=1
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

