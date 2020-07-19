#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (28.60%)
# Likes:    973
# Dislikes: 2385
# Total Accepted:    362.9K
# Total Submissions: 1.3M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x==-1:
            if n%2==0:
                return 1
            else:
                return -1
        isNegative = (n < 0)
        if isNegative:
            n = -n
        ret = 1
        while n > 0:
            if n%2 == 0:
                x = x*x 
                n = n//2
            else:
                ret *= x
                n -= 1
        if isNegative:
            return 1/ret
        else:
            return ret


    #     if n == 0:
    #         return 1
    #     if x == 1:
    #         return 1
    #     if x ==-1:
    #         if n%2 == 0:
    #             return 1 
    #         else:
    #             return -1
    #     if n < 0:
    #         return 1/self.rec_pow(x, -n)
    #     else:
    #         return self.rec_pow(x, n)
        
    # def rec_pow(self, x, n):
    #     if n == 0:
    #         return 1
    #     if n%2==0:
    #         return self.rec_pow(x*x, n//2)
    #     else:
    #         return x*self.rec_pow(x*x, n//2)


    #     res = 0
    #     if n == 0:
    #         return 1
    #     if x == 1:
    #         return 1
    #     if x == -1:
    #         if n % 2 ==0:
    #             return 1
    #         else:
    #             return -1
    #     elif n<0:
    #         n = -n
    #         res = 1/self.rec_pow(x, n)
    #     else:
    #         res = self.rec_pow(x, n)
    #     return res
        
    # def rec_pow(self, x, n):
    #     # n is always positive
    #     if n == 0:
    #         return 1
    #     if n % 2 ==0:
    #         return self.rec_pow(x*x, n//2)
    #     else:
    #         return x*self.rec_pow(x*x, n//2)
          
        
# @lc code=end

