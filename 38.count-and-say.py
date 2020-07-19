#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (41.40%)
# Likes:    905
# Dislikes: 7105
# Total Accepted:    317.9K
# Total Submissions: 759.7K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # print the result row by row
        s = '1'
        if n ==1:
            return s
        for _ in range(2, n+1):
            count = 1
            newS = ''
            s = s+ '*'
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    count+=1
                else:
                    newS += (str(count) + s[i])
                    count = 1
            s = newS
        return s

        # s = '1'
        # if n == 1:
        #     return s
        # for i in range(2,n+1):
        #     count = 1
        #     newS = []
        #     s=s+'*'# add something at the end to make the loop simple
        #     for j in range(len(s)-1):
        #         if s[j]==s[j+1]:
        #             count+=1
        #         else:
        #             newS.append(str(count))
        #             newS.append(s[j])
        #             count = 1
        #     s = ''.join(newS)
        
        # return s
                
# @lc code=end

