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
        self.getCombination(n,k,1,res,[])
        return res

    def getCombination(self, n, k, start, res, res_rec):
        if len(res_rec) == k:
            res.append(list(res_rec))
            return
        if len(res_rec) + n - start + 1 < k:
            return
        if len(res_rec) + n - start + 1== k:
            res.append(res_rec + list(range(start, n+1)))
            return
        for i in range(start, n+1):
            res_rec.append(i)
            self.getCombination(n,k,i+1,res,res_rec)
            res_rec.pop()
        
        return


# @lc code=end

