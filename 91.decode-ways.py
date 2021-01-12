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
        visit = {}
        return self.countDecodings(s, len(s), visit, 0)

    def countDecodings(self, s, sLen, visit, idx):
        if idx == sLen:
            return 1
        if s[idx] == '0':
            return 0
        if idx in visit:
            return visit[idx]
        count1 = self.countDecodings(s, sLen, visit, idx+1)
        count2 = 0
        if idx < sLen-1 and int(s[idx:idx+2])<=26:
            count2 = self.countDecodings(s, sLen, visit, idx+2)
        visit[idx] = count1+count2
        return visit[idx]

            
        
# @lc code=end

