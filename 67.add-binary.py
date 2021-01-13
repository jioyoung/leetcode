#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (40.69%)
# Likes:    1175
# Dislikes: 220
# Total Accepted:    344.3K
# Total Submissions: 844.8K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 二进制 binary 相加
        idx_a = len(a)-1
        idx_b = len(b)-1
        value = 0
        carry = 0
        res = ''
        while idx_a >= 0 or idx_b >=0:
            value = carry # value = carry, iniliaze it to zero + carry
            if idx_a>=0:
                value+=int(a[idx_a])
                idx_a-=1
            if idx_b>=0:
                value+=int(b[idx_b])
                idx_b-=1
            if value > 1:
                value -= 2
                carry = 1
            else:
                carry = 0
            res = str(value) + res
        if carry:
            res = '1' + res
        return res
        
# @lc code=end

