#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charDict = {}
        for i, c in enumerate(order):
            charDict[c] = i
        for i in range(1, len(words)):
            result = self.isTwoWordsEqualorAscending(words[i-1], words[i], charDict)
            if result == False:
                return False
        return True
    
    def isTwoWordsEqualorAscending(self, word1, word2, charDict):
        len1 = len(word1)
        len2 = len(word2)
        length = min(len1, len2)
        for i in range(length):
            if charDict[word1[i]] == charDict[word2[i]]:
                continue
            elif charDict[word1[i]] < charDict[word2[i]]:
                return True
            else:
                return False
        if len1 > len2:
            return False
        

# @lc code=end

