#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nRow = len(matrix)
        if nRow == 0:
            return 0
        nCol = len(matrix[0])
        if nCol == 0:
            return 0
        visit = [[False for j in range(nCol)] for i in range(nRow)]
        countDict = {}
        maxL = 1
        parent = float('-inf') 
        for i in range(nRow):
            for j in range(nCol):
                count = self.getLongestLength(matrix, i, j, nRow, nCol, visit, countDict, parent)
                if count > maxL:
                    maxL = count
        return maxL

    def getLongestLength(self, matrix, iRow, iCol, nRow, nCol, visit, countDict, parent):
        if iRow < 0 or iCol < 0 or iRow == nRow or iCol == nCol or matrix[iRow][iCol]<=parent:
            return 0
        if visit[iRow][iCol]:
            return 0
        index = iRow*nCol+iCol
        if index in countDict:
            return countDict[index]
        visit[iRow][iCol] = True
        current = matrix[iRow][iCol]
        count1 = self.getLongestLength(matrix, iRow+1, iCol, nRow, nCol, visit, countDict, current)
        count2 = self.getLongestLength(matrix, iRow-1, iCol, nRow, nCol, visit, countDict, current)
        count3 = self.getLongestLength(matrix, iRow, iCol+1, nRow, nCol, visit, countDict, current)
        count4 = self.getLongestLength(matrix, iRow, iCol-1, nRow, nCol, visit, countDict, current)
        visit[iRow][iCol] = False
        countDict[index] = 1 + max(count1, count2, count3, count4)
        return countDict[index]
# @lc code=end

