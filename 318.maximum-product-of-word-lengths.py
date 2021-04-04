#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = len(words)
        codes = [0 for i in range(length)]
        for i, oneWord in enumerate(words):
            value = 0
            for c in oneWord:
                value |= 1 << (ord(c) - ord('a'))
            codes[i] = value
        res = 0
        for i in range(length):
            for j in range(i, length):
                if codes[i] & codes[j] == 0:
                    res = max(res, len(words[i]*len(words[j])))
        return res
        
# @lc code=end

