#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (44.21%)
# Likes:    1027
# Dislikes: 363
# Total Accepted:    270.1K
# Total Submissions: 602.8K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# str(int)  ord(char)  int('5')
# 行列小方块 加入 set 里 

'''
str_row = '('+str(i)+')'+c
str_col = c+'('+str(j)+')'
str_sq = '('+str(i//3)+')' + '('+str(j//3)+')' + c
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        visit = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c=='.':
                    continue
                str_row = '(' + str(i) + ')' + c
                str_col = c+ '(' + str(j) + ')'
                str_square = '(' + str(i//3) + ')' + '(' + str(j//3) + ')' +c
                if (str_row in visit) or (str_col in visit) or (str_square in visit):
                    return False
                visit.update({str_row, str_col, str_square})
        return True
        
        
        
        # visit = set()
        # for i in range(9):
        #     for j in range(9):
        #         c = board[i][j]
        #         if c=='.':
        #             continue
        #         str_row = '('+str(i)+')'+c
        #         str_col = c+'('+str(j)+')'
        #         str_sq = '('+str(i//3)+')' + '('+str(j//3)+')' + c
        #         if (str_row in visit) or (str_col in visit) or (str_sq in visit):
        #             return False
        #         else:
        #             visit.update({str_row,str_col,str_sq}) 
        # return True

        

