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
        if n == 1:
            return '1'
        fact_arr = [None for i in range(n-1)]
        fact_arr[0] = 1
        for i in range(1, n-1):
            fact_arr[i] = (i+1)*fact_arr[i-1]
        nums = list(range(1,n+1))
        res = []
        self.getRes(nums, k, res, fact_arr)
        return ''.join(res)

    def getRes(self, nums, k, res, fact_arr):
        numsL = len(nums)
        if numsL == 1:
            res.append(str(nums[0]))
            return
        else:
            nGroup = (k-1)//fact_arr[numsL-2]
            res.append(str(nums.pop(nGroup)))
            k = (k-1) % fact_arr[numsL-2] + 1 # 1 needs to be added since k starts from 1
            self.getRes(nums, k, res, fact_arr)



    #     # if n == 1 then [0]*(n-1) bug; seperately consider it
    #     if n==1:
    #         return '1'
    #     fact_arr = [0]*(n-1)
    #     fact_arr[0]=1
    #     for i in range(1, n-1):
    #         fact_arr[i]=(i+1)*fact_arr[i-1]
    #     nums = list(range(1,n+1))
    #     res = []
    #     # int list to string: every time append a str(int) then at last ''.join(list)
    #     self.getRes(nums, k, res,fact_arr)
    #     return ''.join(res)
    
    # def getRes(self, nums, k, res,fact_arr):
    #     numsL = len(nums)
    #     if numsL==1:
    #         res.append(str(nums[0]))
    #         return
    #     group = (k-1)//fact_arr[numsL-2] # the corresponding index numsL-2
    #     res.append(str(nums.pop(group)))
    #     remain = (k-1) % fact_arr[numsL-2]
    #     k = remain + 1
    #     self.getRes(nums, k, res, fact_arr)
        
        
        
        
# @lc code=end

