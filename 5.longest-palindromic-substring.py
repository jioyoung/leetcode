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
    def longestPalindrome(self, s):
        # maxLen = 1
        # start = 0
        # dp_pal = [[False for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     dp_pal[i][i] = True
        #     for j in range(i):
        #         if i == j+1:
        #             dp_pal[j][i] = (s[i]==s[j])
        #         else:
        #             # i > j+1
        #             if s[j] == s[i] and dp_pal[j+1][i-1]:
        #                 dp_pal[j][i] = True
        #         if dp_pal[j][i] and i-j+1>maxLen:
        #             maxLen = i-j+1
        #             start = j
        # return s[start:start+maxLen]
        sLen = len(s)
        res = ""
        for i in range(sLen):
            temp = self.outputPalindrome(s, sLen, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.outputPalindrome(s, sLen, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res

    def outputPalindrome(self, s, sLen, l, r):
        while l>=0 and r<sLen and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]






