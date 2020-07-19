#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (43.01%)
# Likes:    3667
# Dislikes: 133
# Total Accepted:    495.7K
# Total Submissions: 1.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
'''
bfs 或者 dfs找到成片的 1 即可
找的过程中把visit 过的1 变成2 避免重复count
'''
# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        nrow = len(grid)
        if nrow == 0:
            return 0
        ncol = len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]=='1':
                    count+=1
                    self.mark_one_BFS(i, j, nrow, ncol, grid)
                    '''
                    bfs dfs 都可以
                    # self.mark_one_DFS(i, j, nrow, ncol, grid) bfs
                    '''
        
        return count
        
    def mark_one_DFS(self, iRow, iCol, nRow, nCol, matrix):
        if iRow < 0 or iCol < 0 or iRow == nRow or iCol == nCol or matrix[iRow][iCol]!='1':
            return
        matrix[iRow][iCol]='2'
        self.mark_one_DFS(iRow-1, iCol, nRow, nCol, matrix)
        self.mark_one_DFS(iRow+1, iCol, nRow, nCol, matrix)
        self.mark_one_DFS(iRow, iCol-1, nRow, nCol, matrix)
        self.mark_one_DFS(iRow, iCol+1, nRow, nCol, matrix)
    
    def mark_one_BFS(self, iR, iC, nR, nC, matrix):
        queue = []
        queue.append(iR*nC + iC)
        while queue:
            cur = queue.pop(0)
            row = cur // nC
            col = cur % nC
            if matrix[row][col]=='2':
                #visited
                continue
            matrix[row][col]='2'
            if row > 0 and matrix[row-1][col]=='1':
                queue.append((row-1)*nC+col)
            if row < nR-1 and matrix[row+1][col]=='1':
                queue.append((row+1)*nC+col)
            if col > 0 and matrix[row][col-1]=='1':
                queue.append((row)*nC+col-1)
            if col < nC-1 and matrix[row][col+1]=='1':
                queue.append((row)*nC+col+1)


# @lc code=end

