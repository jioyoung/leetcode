#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (32.46%)
# Likes:    721
# Dislikes: 2128
# Total Accepted:    425.5K
# Total Submissions: 1.3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        sLen = len(s)
        left = 0
        right = sLen - 1
        while left < right:
            while (not s[left].isalpha()) and (not s[left].isnumeric()):
                left+=1
                if left == sLen:
                    return True
            while (not s[right].isalpha()) and (not s[right].isnumeric()):
                right-=1
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

        
        
# @lc code=end

