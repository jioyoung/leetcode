#
# @lc app=leetcode id=132 lang=python
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (28.35%)
# Likes:    832
# Dislikes: 28
# Total Accepted:    119K
# Total Submissions: 409.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        valid = [[False for i in range(length)] for j in range(length)]
        for one_len in range(length):
            for i in range(length-one_len):
                j = i+one_len
                valid[i][j] = s[i]==s[j] and (one_len<=2 or valid[i+1][j-1])
        
    '''
    https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-132-palindrome-partitioning-ii/
    subproblem + palindrome
    '''
        cut = [length-1]*length
        for i in range(length):
            if valid[0][i]:
                cut[i]=0
                continue
            for j in range(i):
                if valid[j+1][i]:
                    cut[i] = min(cut[i], cut[j]+1)
        return cut[-1]
        
# @lc code=end

