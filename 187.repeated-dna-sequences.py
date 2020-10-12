#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visitSet = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:10+i] in visitSet:
                res.add(s[i:10+i])
            else:
                visitSet.add(s[i:10+i])
        return list(res)
# @lc code=end

