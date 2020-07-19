#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        if n == 0:
            return res
        for i in range(n):
            value = 1<<i
            resL = len(res)
            for j in range(resL-1,-1,-1):
                res.append(res[j]+value)
        return res
        
# @lc code=end

