#
# @lc app=leetcode id=132 lang=python
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (28.35%)
# Likes:    832
# Dislikes: 28
# Total Accepted:    119K
# Total Submissions: 409.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 回文 切割
        # valid_dp 表示 s[i:j+1] 是否是回文
        # min_cut[j]表示 s[0:j+1]要几刀才都是回文
        valid_dp = [[False for j in range(len(s))] for i in range(len(s))]
        for length in range(len(s)):
            for i in range(len(s)-length):
                j = i+length
                valid_dp[i][j]=(s[i]==s[j]) and (length<=2 or valid_dp[i+1][j-1])
        min_cut = [len(s)-1] * len(s)
        for j in range(len(s)):
            if valid_dp[0][j]:
                min_cut[j] = 0
                continue
            for i in range(j):
                if valid_dp[i+1][j]:
                    min_cut[j] = min(min_cut[j], min_cut[i]+1)
        return min_cut[-1]
# @lc code=end

