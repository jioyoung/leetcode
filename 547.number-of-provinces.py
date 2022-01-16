#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visit = set()
        length = len(isConnected)
        for i in range(length):
            if i not in visit:
                res+=1
                self.dfs_circle(isConnected, length, i, visit)
        return res        
    
    def dfs_circle(self, M, length, i, visit):
        visit.add(i)
        for j in range(length):
            if M[i][j] == 0 or j in visit:
                continue
            else:
                self.dfs_circle(M, length, j, visit)
        return


# @lc code=end

