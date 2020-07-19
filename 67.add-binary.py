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
        res = []
        id_a = len(a)-1
        id_b = len(b)-1
        carry = 0
        while id_a>=0 or id_b>=0:
            if id_a >=0:
                c_a = int(a[id_a])
            else:
                c_a = 0 
            if id_b >=0:
                c_b = int(b[id_b])
            else:
                c_b = 0 
            sum_c_ab = c_a+c_b+carry
            if sum_c_ab > 1:
                carry = 1
            else:
                carry = 0
            res.append(str(sum_c_ab % 2))
            id_a-=1
            id_b-=1
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
        # 不可以直接 ''.join(res.reverse())
        # res.reverse() 改变的是 res本身
            
            
        
# @lc code=end

