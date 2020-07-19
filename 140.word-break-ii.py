#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (28.32%)
# Likes:    1448
# Dislikes: 320
# Total Accepted:    197.8K
# Total Submissions: 669.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        '''
        这样也通过了，，，真的蠢
        先判断能不能breakable 和 139 一样 用dp
        然后再用一次dp 记录parent 的index
        最后把目标index组变成string
        
        '''

        if not self.breakable(s, wordDict):
            return []
        dp = {}
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = [[i]]

        for i in range(1,len(s)):
            if (i-1) in dp:
                for j in range(i, len(s)):
                    if s[i:j+1] in wordDict:
                        if j not in dp:
                            dp[j]=[]
                        for alist in dp[i-1]:
                            dp[j].append(alist+[j])
                del dp[i-1]
        if len(s)-1 not in dp:
            return []
        ret = []
        for aList in dp[len(s)-1]:
            temp=[]
            num = len(aList)
            for i in range(num):
                if i == 0:
                    temp.append(s[:aList[i]+1])
                else:
                    temp.append(s[aList[i-1]+1:aList[i]+1])
            ret.append(' '.join(temp))
        return ret

    def breakable(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        '''
        dynamic programming
        dp[i] true is s[0:i-1] can be constructed
        form the words in the dict
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

