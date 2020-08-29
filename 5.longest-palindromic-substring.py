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
        maxLen = 1
        start = 0
        dp_pal = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp_pal[i][i] = True
            for j in range(i):
                if i == j+1:
                    dp_pal[j][i] = (s[i]==s[j])
                else:
                    # i > j+1
                    if s[j] == s[i] and dp_pal[j+1][i-1]:
                        dp_pal[j][i] = True
                if dp_pal[j][i] and i-j+1>maxLen:
                    maxLen = i-j+1
                    start = j
        return s[start:start+maxLen]


