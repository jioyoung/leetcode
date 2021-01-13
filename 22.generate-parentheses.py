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
        # 构建 构造 括号 parenthesis
        #backtrack
        res = []
        self.getRes(0,0,n,res, [])
        return res
        
        
    def getRes(self, nLeft, nRight, n, res, rec_res):
        if len(rec_res) == 2*n:
            res.append(''.join(rec_res))
            return
        if nLeft < n:
            rec_res.append('(')
            self.getRes(nLeft+1, nRight, n, res, rec_res)
            rec_res.pop()
        if nLeft > nRight:
            rec_res.append(')')
            self.getRes(nLeft, nRight+1, n, res, rec_res)
            rec_res.pop()
        return



