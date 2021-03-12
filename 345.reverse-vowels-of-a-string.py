#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelArr = [c for c in s if c in 'aeiouAEIOU']
        i = len(vowelArr) - 1
        s2 = list(s)
        for j in range(len(s)):
            if s2[j] in 'aeiouAEIOU':
                s2[j] = vowelArr[i]
                i-=1
        return ''.join(s2)
# @lc code=end

