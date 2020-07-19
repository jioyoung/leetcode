#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.40%)
# Likes:    3294
# Dislikes: 198
# Total Accepted:    393.7K
# Total Submissions: 689.6K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# zy: dfs
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        #backtrack
        # here no need to backtrack since every time a new string is generated
        # by adding two strings
        result = []
        self.generate(0, 0, result, '', n)
        return result

    def generate(self, nLeft, nRight, result, str_rec, n):
        if len(str_rec) == 2*n:
            result.append(str_rec)
            return
        if nLeft < n:
            self.generate(nLeft+1, nRight, result, str_rec+'(', n)
        if nRight < nLeft:
            self.generate(nLeft, nRight+1, result, str_rec+')', n)


    #     res = []
    #     rec_res = []
    #     self.generate(0, 0, res, rec_res, n)
    #     return res

    # def generate(self, nLeft, nRight, res, rec_res, n):
    #     if len(rec_res) == n*2:
    #         res.append(''.join(rec_res))
    #         return
    
    #     if nLeft < n:
    #         rec_res.append('(')
    #         self.generate(nLeft+1,nRight,res, rec_res, n)
    #         # 一定要这一步 回溯
    #         rec_res.pop()
    #     if nRight < nLeft:
    #         rec_res.append(')')
    #         self.generate(nLeft,nRight+1,res, rec_res, n)
    #         rec_res.pop()


