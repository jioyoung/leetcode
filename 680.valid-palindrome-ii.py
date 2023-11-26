#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.verifyPalindrome(s[left+1:right+1]) \
                    or self.verifyPalindrome(s[left:right])
        return True

    def verifyPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
        
# @lc code=end

