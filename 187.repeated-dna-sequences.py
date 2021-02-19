#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        visitSet = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in visitSet:
                visitSet.add(s[i:i+10])
            else:
                res.add(s[i:i+10])
        return list(res)
            
# @lc code=end

