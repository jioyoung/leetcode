#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (34.20%)
# Likes:    989
# Dislikes: 266
# Total Accepted:    151.8K
# Total Submissions: 443.5K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 排列 第k大的排列 排列
        if n == 1:
            return '1'
        factArr = [None]*(n-1)
        factArr[0] = 1
        for i in range(1, n-1):
            factArr[i] = (i+1)*factArr[i-1]
        factIdx = n-2
        nums = [i for i in range(1, n+1)]
        res = ''
        while factIdx >= 0:
            nGroup = (k-1)//factArr[factIdx]
            candidate = nums.pop(nGroup)
            res = res + str(candidate)
            k = k % factArr[factIdx]
            factIdx -= 1
        res = res + str(nums[0])
        return res



# @lc code=end

