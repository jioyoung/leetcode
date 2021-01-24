#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (53.16%)
# Likes:    826
# Dislikes: 45
# Total Accepted:    146.8K
# Total Submissions: 270.5K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 组合的和 combination sum
        if k == 1:
            if n >=1 and n <= 9:
                return [[n]]
            else:
                return []
        if k > 9:
            return []
        maxSum = 0
        for i in range(9,9-k,-1):
            maxSum += i
        if maxSum < n:
            return []
        res = []
        minSum = 0
        for i in range(1, k):
            minSum+=i
        right = min(9, n-minSum)
        self.getResult(k, n, 1, right, res, [])
        return res
    
    def getResult(self, k, n, left, right, res, rec_res):
        # k is the number of values remaining
        # left is the smallest value that can be used
        # right is the largest
        # for one combination, all values are increasing
        # n is the target sum
        # ret is the result
        if k == 0 and n ==0:
            res.append(list(rec_res))
            return
        if k == 0 or n == 0:
            return
        if left > right:
            return
        for i in range(left, right+1):
            rec_res.append(i)
            self.getResult(k-1, n-i, i+1,right, res, rec_res)
            rec_res.pop()
        return 

# @lc code=end

