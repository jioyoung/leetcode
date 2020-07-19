#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (36.70%)
# Likes:    3352
# Dislikes: 182
# Total Accepted:    454.9K
# Total Submissions: 1.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        '''
        dynamic programming
        dp[i] true is s[0:i-1] can be constructed form the words in the dict
        dp[j] = dp[i] && dp[i+1, j]
        '''
        dp = [True] + [False]*len(s)
        for start in range(len(s)):
            if dp[start]:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        dp[end] = True
                        if end == len(s):
                            return True
        return dp[-1]

        
# @lc code=end

