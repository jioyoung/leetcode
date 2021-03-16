#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

'''
    dynamic programming
    f[i][j] is if the string between i th and j th is palindromic
    f[i][j] = true if i == j
            = S[i] == S[j] if j == i + 1
            = S[i] == S[j] && f[i+1][j-1] if j > i+1
    1st iteration: j = range(len(s))
    2nd iteration: i = range(j) 
'''

class Solution:
    # 最长 回文 最长回文
    def longestPalindrome(self, s):
        maxLen = 1
        start = 0
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if i == j+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    if s[i] == s[j] and dp[j+1][i-1]:
                        dp[j][i] = True
                if dp[j][i] and i-j+1> maxLen:
                    maxLen = i-j+1
                    start = j
        return s[start:start+maxLen]
    #     sLen = len(s)
    #     res = ''
    #     maxL = 0
    #     for i in range(sLen):
    #         temp = self.outputPalindrome(i, i, s, sLen)
    #         if len(temp) > maxL:
    #             res = temp
    #             maxL = len(temp)
    #         temp = self.outputPalindrome(i, i+1, s, sLen)
    #         if len(temp) > maxL:
    #             res = temp
    #             maxL = len(temp)
    #     return res

    # def outputPalindrome(self, left, right, s, sLen):
    #     while left >= 0 and right < sLen and s[left] == s[right]:
    #         left-=1
    #         right+=1
    #     return s[left+1:right]
        



    






