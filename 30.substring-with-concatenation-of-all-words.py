#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.98%)
# Likes:    626
# Dislikes: 1009
# Total Accepted:    146.5K
# Total Submissions: 606.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # the complexity is O(n*m)
        # m is the # word in words
        # n is the length of s
        wordCount = {}
        for oneWord in words:
            wordCount[oneWord] = wordCount.get(oneWord, 0) + 1
        nWord = len(words)
        wordLen = len(words[0])
        strLen = nWord * wordLen
        res = []
        for i in range(len(s) - strLen + 1):
            count = 0
            newStrCount = {}
            for start in range(i, i+strLen, wordLen):
                candidate = s[start:start+wordLen]
                if candidate not in wordCount:
                    break
                else:
                    newStrCount[candidate] = newStrCount.get(candidate, 0) + 1
                    if newStrCount[candidate] > wordCount[candidate]:
                        break
                    count += 1
                if count == nWord:
                    res.append(i)
        return res
        
# @lc code=end

