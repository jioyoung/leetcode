#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (49.96%)
# Likes:    953
# Dislikes: 56
# Total Accepted:    230.6K
# Total Submissions: 460.7K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        rec_res = []
        self.generateRes(n, k, 1, res, rec_res)
        return res
    
    def generateRes(self, n, k, start, res, rec_res):
        if len(rec_res)==k:
            res.append(list(rec_res))
            return
        if n-start+1<k-len(rec_res):
            return
        if n-start+1==k-len(rec_res):
            rec_res1 = rec_res+list(range(start,n+1))
            res.append(list(rec_res1))

            return

        for i in range(start,n+1):
            rec_res.append(i)
            self.generateRes(n, k, i+1, res, rec_res)
            rec_res.pop() 
    
# @lc code=end

