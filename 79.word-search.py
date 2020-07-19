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
        n_r = len(board)
        if n_r == 0:
            return False
        n_c = len(board[0])
        if n_c == 0:
            return False
        visit = [None]*n_r
        for i in range(n_r):
            visit[i] = [0]*n_c
        
        for i in range(n_r):
            for j in range(n_c):
                if self.dfs(board, n_r, n_c,word, visit, 0, i, j):
                    return True
        return False
        
    def dfs(self, board, nr, nc, word, visit, index, i_r, i_c):
        if index == len(word):
            return True
        if i_r < 0 or i_c < 0 or i_r >=nr or i_c >=nc:
            return False
        if visit[i_r][i_c]==1:
            return False
        if board[i_r][i_c]!=word[index]:
            return False
        else:
            visit[i_r][i_c]=1
            res = 0
            res = (self.dfs(board, nr, nc, word, visit, index+1, i_r+1, i_c) or \
                    self.dfs(board, nr, nc, word, visit, index+1, i_r, i_c+1) or \
                    self.dfs(board, nr, nc, word, visit, index+1, i_r-1, i_c) or \
                    self.dfs(board, nr, nc, word, visit, index+1, i_r, i_c-1))
            visit[i_r][i_c]=0
            return res

