#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (32.86%)
# Likes:    1191
# Dislikes: 3626
# Total Accepted:    361.6K
# Total Submissions: 1.1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # this is to find the rules 
        # pay attention to 2nd to (largest-1)th row

        sLen = len(s)
        if sLen <=numRows or numRows ==1:
            return s
        nCycle = 2*(numRows-1)
        str_arr = ''
        for i in range(numRows):
            for j in range(i, sLen, nCycle):
                str_arr+=s[j]
                if i>0 and i<numRows-1:
                    iExtra = j + nCycle - 2*i
                    if iExtra < sLen:
                        str_arr+=s[iExtra]
        return str_arr

        # sLen = len(s)
        # str = []
        # if sLen<=numRows or numRows<2:
        #     return s
        # lag = 2 * (numRows-1)
        # for i in range(numRows):
        #     for j in range(i, sLen, lag):
        #         str.append(s[j])
        #         if i>0 and i<numRows-1:
        #             iExtra = j+lag-2*i
        #             if iExtra < sLen:
        #                 str.append(s[iExtra])
        # return ''.join(str)





