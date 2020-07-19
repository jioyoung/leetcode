#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (29.62%)
# Likes:    886
# Dislikes: 184
# Total Accepted:    192.3K
# Total Submissions: 643.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        26进制 但是是从1到26 不是0到25 所以如果余数等于0 要处理一哈
        """
        res =''
        while n>0:
            r = n%26
            if r == 0:
                r = 26
                n = n-1
            res = chr(ord('A')+r-1)+res
            n = n//26
        return res
        
# @lc code=end

