#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        visitSet = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in visitSet:
                visitSet.add(s[i:i+10])
            else:
                if s[i:i+10] not in res:
                    res.append(s[i:i+10])
        return res
# @lc code=end

