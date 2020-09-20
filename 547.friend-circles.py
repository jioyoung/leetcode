#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        res = 0
        n = len(M)
        visit = [0]*n
        for i in range(n):
            if visit[i] == 1:
                continue
            res+=1
            self.visitFriend(visit, i, M, n)

        return res
    
    def visitFriend(self, visit, i, M, n):
        visit[i] = 1
        for j in range(n):
            if M[i][j] == 0 or visit[j] == 1:
                continue
            else:
                self.visitFriend(visit, j, M, n)
    



# @lc code=end

