#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (42.87%)
# Likes:    1278
# Dislikes: 51
# Total Accepted:    192.7K
# Total Submissions: 439.7K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 回文 切割
        #分治的思想
        # valid_dp 表示 s[i:j+1] 是否是回文
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for length in range(0, len(s)):
            for i in range(0, len(s)-length):
                j = i+length
                dp[i][j]=(s[i]==s[j]) and (length<=2 or dp[i+1][j-1])
        
        # dp[i][j] is Boolean whether s[i:j+1] is pal
        result = []
        self.dfs(s, 0, len(s)-1, [], result, dp)
        return result

    def dfs(self, s, start, end, rec_res, result, dp):
        if start>end:
            result.append(list(rec_res))
            return
        for j in range(start, end+1):
            if dp[start][j]:
                rec_res.append(s[start:j+1])
                self.dfs(s, j+1, end, rec_res, result, dp)
                rec_res.pop()
        return

# @lc code=end

