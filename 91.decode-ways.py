#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.94%)
# Likes:    1728
# Dislikes: 1969
# Total Accepted:    300.6K
# Total Submissions: 1.3M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        visit = dict()
        return self.countDecodings(0, s, len(s), visit)
        
    
    def countDecodings(self, index, s, sLen, visit):
        if index == sLen:
            return 1
        if s[index]=='0':
            return 0
        # select index
        if index in visit:
            return visit[index] 
        a = self.countDecodings(index+1, s, sLen, visit)
        b = 0
        if index < sLen-1:
            if 10*(ord(s[index])-ord('0'))+(ord(s[index+1])-ord('0'))<=26:
                b = self.countDecodings(index+2, s, sLen, visit)
        
        visit[index] = a+b
        return a+b

            
        
# @lc code=end

