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
        canBreak = self.canBreak(s, wordDict)
        if canBreak == False:
            return []
        
        validEnd = {}
        validEnd[0] = [[0]]
        
        # [0,1,2,3,4,5]
        
        for start in range(len(s)):
            if start in validEnd:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        if end in validEnd:
                            for oneList in validEnd[start]:
                                validEnd[end].append(oneList+[end])
                        else:
                            validEnd[end] = []
                            for oneList in validEnd[start]:
                                validEnd[end].append(oneList+[end])
                del validEnd[start]
        
        res = []
        
        for oneList in validEnd[len(s)]:
            temp = []
            for i in range(1, len(oneList)):
                start = oneList[i-1]
                end = oneList[i]
                temp.append(s[start:end])

            res.append(' '.join(temp))
        return res
    
    def canBreak(self, s, wordDict):
        validEnd= set([0])
        for start in range(len(s)):
            if start in validEnd:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        validEnd.add(end)
                        if end == len(s):
                            return True
        return False


# @lc code=end

