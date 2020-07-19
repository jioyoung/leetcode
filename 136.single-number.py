#
<<<<<<< HEAD
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start

'''
牛逼
异或运算的几个相关公式：

1. a ^ a = 0
2. a ^ b = b ^ a
3. a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c
4. d = a ^ b ^ c 可以推出 a = d ^ b ^ c
5. a ^ b ^ a = b
 
本题可以抽象成：数组里有x1, x2 ... xn（每个出现2次），和y（只出现一次），得出y的值。
由公式2可知，数组里面所有数异或的结果等于 x1^x1^x2^x2^...^xn^xn^y
由公式3可知，上式等于(x1^x1)^(x2^x2)^...^(xn^xn)^y
由公式1可知，上式等于(0)^(0)^...(0)^y = y
————————————————
版权声明：本文为CSDN博主「隐之狐」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hf81970/article/details/13630769
'''

class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[i] ^=nums[i-1]
    
        return nums[-1]
=======
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (61.55%)
# Likes:    3385
# Dislikes: 133
# Total Accepted:    615K
# Total Submissions: 980.7K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^=nums[i]
        return answer
>>>>>>> fb7103779365f5d4964fc2e056d5fdf7f1825ad6
        
# @lc code=end

