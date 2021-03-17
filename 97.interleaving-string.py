#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        我们定义一个 boolean 二维数组 dp [ i ] [ j ] 
        来表示 s1[ 0, i ) 和 s2 [ 0, j ） 
        组合后能否构成 s3 [ 0, i + j )，
        注意不包括右边界，主要是为了考虑开始的时候如果只取 s1，
        那么 s2 就是空串，这样的话 dp[i][0] 就能表示 s2 取空串。
        状态转换方程也很好写了，如果要求 dp [i] [j] 。
        如果 dp [i-1][j] == true，并且 s1[i-1] == s3[i+j-1]，dp[i][j]=true 。
        如果 dp [i][j-1]==true，并且 s2[j-1]==s3[i+j-1] dp[i][j]=true 。
        否则的话，就更新为 dp[i][j] = false。
        '''        
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for j in range(len(s2)+1):
            for i in range(len(s1)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                        (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
# @lc code=end

