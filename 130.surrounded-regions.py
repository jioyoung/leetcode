#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (24.10%)
# Likes:    1039
# Dislikes: 517
# Total Accepted:    173.5K
# Total Submissions: 703.3K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        if nrow == 0:
            return 
        ncol = len(board[0])
        for i in range(nrow):
            for j in range(ncol):
                if i == 0 or i == nrow-1 or j == 0 or j == ncol-1:
                    if board[i][j] == 'O':
                        self.mark_O_side(i, j, nrow, ncol, board)
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

    
    def mark_O_side(self, iRow, iCol, nRow, nCol, board):
        #DFS
        if iRow < 0 or iCol < 0 or iRow == nRow or iCol == nCol or board[iRow][iCol]!='O':
            return
        
        board[iRow][iCol]='*'
        self.mark_O_side(iRow+1, iCol, nRow, nCol, board)
        self.mark_O_side(iRow-1, iCol, nRow, nCol, board)
        self.mark_O_side(iRow, iCol+1, nRow, nCol, board)
        self.mark_O_side(iRow, iCol-1, nRow, nCol, board)

        
# @lc code=end

