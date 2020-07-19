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
 1st iteration: j =range(len(s))
 2nd iteration: i = range(j) 
'''

class Solution:
    def longestPalindrome(self, s):
        sLen = len(s)
        maxLen = 1
        start = 0
        helper = [None]*sLen
        for i in range(sLen):
            helper[i]=[None]*sLen
        for j in range(sLen):
            helper[j][j] = True
            for i in range(j):
                if j == i+1:
                    helper[i][j] = s[i]==s[j]
                else:
                    # j > i+1
                    helper[i][j] = (s[i]==s[j]) and helper[i+1][j-1] 
                if helper[i][j] and j-i+1>maxLen:
                    start = i
                    maxLen = j-i+1
        return s[start:start+maxLen]






        # sLen = len(s)
        # dp = [None]*sLen
        # for i in range(sLen):
        #     dp[i]=[None]*sLen
        # #now dp is a n*n matrix
        # max_len = 1
        # start = 0

        # for j in range(sLen):
        #     dp[j][j] = True 
        #     for i in range(j):
        #         dp[i][j] = (s[i]==s[j]) and (j < i+2 or dp[i+1][j-1])
        #         if dp[i][j]:
        #             if (j-i+1) > max_len:
        #                 max_len = j-i+1
        #                 start = i
        # return s[start:start+max_len]

        
        

