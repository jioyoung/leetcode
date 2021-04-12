#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        subLen = length//2
        for subStrLen in range(1, subLen+1):
            if length%subStrLen==0:
                for i in range(1, length//subStrLen):
                    str1 = s[(i-1)*subStrLen: i*subStrLen]
                    str2 = s[i*subStrLen: (i+1)*subStrLen]
                    if str1 == str2:
                        if i == length//subStrLen-1:
                            return True
                        continue
                    else:
                        break
        return False
# @lc code=end

