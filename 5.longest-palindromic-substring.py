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
        for length in range(0, len(s)):
            for i in range(0, len(s)-length):
                j = i+length
                if (s[i]==s[j]) and (length<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1> maxLen:
                        maxLen = j-i+1
                        start = i
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
        



    






