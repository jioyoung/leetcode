#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        '''
        dp = m*[1]
        for j in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[-1] 

