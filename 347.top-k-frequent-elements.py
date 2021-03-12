#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valueCount = {}
        for value in nums:
            valueCount[value] = valueCount.get(value, 0) + 1
        countTuple = list(valueCount.items())
        countTuple.sort(reverse=True, key=lambda x:x[1])
        res = []
        for i in range(k):
            res.append(countTuple[i][0])
        return res

        
# @lc code=end

