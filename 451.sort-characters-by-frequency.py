#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        charDict = {}
        for c in s:
            charDict[c] = charDict.get(c, 0) + 1
        charCount = list(charDict.items())
        charCount.sort(key=lambda x: x[1], reverse=True)
        res = ''
        for i in range(len(charCount)):
            res = res + charCount[i][1]*charCount[i][0]
        return res
# @lc code=end

