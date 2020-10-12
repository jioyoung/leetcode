#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 多一维的空间，因为求 dp_matrix[len - 1][j] 的时候需要知道 dp_matrix[len][j] 的情况，
        # 多一维的话，就可以把 对 dp_matrix[len - 1][j] 也写进循环了
        # dp_matrix[i][j]表示 text 从 i 开始到最后，pattern 从 j 开始到最后，
        # 此时 text 和 pattern 是否匹配。
        sLen = len(s)
        pLen = len(p)
        dp_matrix = [[False for j in range(pLen+1)] for i in range(sLen+1)]
        # dp_matrix[len][len] 代表两个空串是否匹配了，"" 和 "" ，当然是 true 了。
        dp_matrix[-1][-1] = True

        # 从 len 开始减少
        for i in range(sLen, -1, -1):
            for j in range(pLen, -1, -1):
                if i == sLen and j == pLen:
                    continue
                # dp_matrix[i][j+2] == True and p[j+1] is *, p[j] can be ignored with 0 repeated times
                # dp_matrix[i+1][j] == True and currentMatch, then dp_matrix[i][j] is also true
                currentMatch = (i < sLen and j < pLen) and \
                    (p[j] == s[i] or p[j] == '.')
                if j + 1 < pLen and p[j+1] == '*':
                    dp_matrix[i][j] = dp_matrix[i][j + 2] or (currentMatch and dp_matrix[i + 1][j])
                else: 
                    dp_matrix[i][j] = currentMatch and dp_matrix[i + 1][j + 1]
        return dp_matrix[0][0]




# @lc code=end

