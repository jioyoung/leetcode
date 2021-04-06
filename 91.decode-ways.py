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
        # 用一个 dp 数组， dp[i] 代表字符串 s[i,s.len-1]
        # 也就是 s 从i开始到结尾的字符串的解码方式。
        # 这样和递归完全一样的递推式。
        # 如果 s[i]和 s[i+1] 组成的数字小于等于 26，那么
        # dp[i]= dp[i+1] + dp [i+2]
        dp = [0 for i in range(len(s)+1)]
        dp[len(s)] = 1
        if s[-1] != '0':
            dp[len(s)-1] = 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                continue
            ans1 = dp[i+1]
            ans2 = 0
            if int(s[i:i+2])<=26:
                ans2 = dp[i+2]
            dp[i] = ans1 + ans2
        return dp[0]

    #     # 密码 字母对应 数字 数量
    #     visit = {}
    #     return self.countDecodings(s, len(s), visit, 0)
    #     # 从 index 开始到结束的数量

    # def countDecodings(self, s, sLen, visit, idx):
    #     if idx == sLen:
    #         return 1
    #     if s[idx] == '0':
    #         # 0 不能开头
    #         return 0
    #     if idx in visit:
    #         return visit[idx]
    #     count1 = self.countDecodings(s, sLen, visit, idx+1)
    #     count2 = 0
    #     if idx < sLen-1 and int(s[idx:idx+2])<=26:
    #         count2 = self.countDecodings(s, sLen, visit, idx+2)
    #     visit[idx] = count1+count2
    #     return visit[idx]

            
        
# @lc code=end

