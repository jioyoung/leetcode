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
        res = []
        recur_res = []
        self.recursiveGenerate(res, recur_res, 0, 0, n)
        return res
    
    def recursiveGenerate(self, res, recur_res, nLeft, nRight, n):
        if len(recur_res) == 2*n:
            res.append(''.join(recur_res))
            return
        if nLeft < n:
            recur_res.append('(')
            nLeft+=1
            self.recursiveGenerate(res, recur_res, nLeft, nRight, n)
            nLeft-=1
            recur_res.pop()
        if nLeft>nRight:
            recur_res.append(')')
            nRight+=1
            self.recursiveGenerate(res, recur_res, nLeft, nRight, n)
            nRight-=1
            recur_res.pop()



