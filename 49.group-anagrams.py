#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (49.60%)
# Likes:    2047
# Dislikes: 132
# Total Accepted:    404.5K
# Total Submissions: 815.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 字谜
        # sort string as a key in the dictionary
        wordDict = {}
        for oneWord in strs:
            temp = ''.join(sorted(oneWord))
            if temp in wordDict:
                wordDict[temp].append(oneWord)
            else:
                wordDict[temp] = [oneWord]
        return wordDict.values()

# @lc code=end

