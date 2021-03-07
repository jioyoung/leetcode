#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = {}
        for oneWord in words:
            wordCount[oneWord] = wordCount.get(oneWord, 0)+1
        wordCountList = list(wordCount.items())
        wordCountList.sort(key=lambda x:(-x[1], x[0]))
        res = []
        for i in range(k):
            res.append(wordCountList[i][0])
        return res
        
# @lc code=end

