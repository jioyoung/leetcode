#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]: longest subset that has i zero and j one
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for oneStr in strs:
            nZero = oneStr.count('0')
            nOne = len(oneStr) - nZero
            for i in range(m, nZero-1, -1):
                for j in range(n, nOne-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-nZero][j-nOne]+1)
        return dp[m][n]


        
# @lc code=end

