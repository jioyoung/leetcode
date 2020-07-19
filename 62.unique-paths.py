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
        if m==1 or n==1:
            return 1
        step_dp = [1 for _ in range(m)]
        for _ in range(1, n):
            for i in range(1,m):
                step_dp[i] += step_dp[i-1]
        return step_dp[m-1]
