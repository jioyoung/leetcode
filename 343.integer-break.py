#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        visit={1:1, 2:1}
        return self.getMaxProduct(n, visit)
        

    def getMaxProduct(self, n, visit):
        if n in visit:
            return visit[n]
        res = 0
        for i in range(1, n):
            val1 = i
            val2 = n - val1
            res = max(res, max(self.getMaxProduct(val1, visit), val1) * max(self.getMaxProduct(val2, visit), val2))
        visit[n] = res
        return res    

# @lc code=end

