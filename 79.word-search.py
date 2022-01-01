#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (31.95%)
# Likes:    1989
# Dislikes: 100
# Total Accepted:    309.1K
# Total Submissions: 967.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 找单词 寻找单词 DFS
        # Time Complexity: \mathcal{O}(N \cdot 3 ^ L)
        # where N is the number of cells in the board and L is the length of the word to be matched.
        # Space Complexity: \mathcal{O}(L) where L is the length of the word to be matched   

        nRow = len(board)
        if nRow == 0:
            return False
        nCol = len(board[0])
        if nCol == 0:
            return False
        visit = [[False for j in range(nCol)] for i in range(nRow)]
        for i in range(nRow):
            for j in range(nCol):
                res = self.searchWord(board, word, i, j, nRow, nCol, visit, 0)
                if res == True:
                    return True
        return False

    def searchWord(self, board, word, iRow, iCol, nRow, nCol, visit, index):
        if index == len(word):
            return True
        if iRow < 0 or iRow == nRow or iCol == nCol or iCol < 0 or board[iRow][iCol]!=word[index]:
            return False
        if visit[iRow][iCol] == True:
            return False
        visit[iRow][iCol] = True
        res = self.searchWord(board, word, iRow-1, iCol, nRow, nCol, visit, index+1) or \
            self.searchWord(board, word, iRow+1, iCol, nRow, nCol, visit, index+1) or \
            self.searchWord(board, word, iRow, iCol-1, nRow, nCol, visit, index+1) or \
            self.searchWord(board, word, iRow, iCol+1, nRow, nCol, visit, index+1)
        visit[iRow][iCol]= False
        return res
