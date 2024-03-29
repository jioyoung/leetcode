#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        slow = fast = 0
        minL = len(s) + 1
        minSlow = 0
        tLen = len(t) # the length of reamining string in t that are not covered in window
        for fast in range(len(s)):
            if s[fast] in tCount:
                tCount[s[fast]]-=1
                if tCount[s[fast]] >= 0:
                    tLen -= 1
                if tLen == 0:
                    # when tLen is 0 it will never increase to positive
                    # the move of slow pointer is guaranteed to cover t
                    while (s[slow] not in tCount) or (tCount[s[slow]] + 1 <= 0):
                        if s[slow] in tCount:
                            tCount[s[slow]] += 1
                        slow += 1
                    length = fast - slow + 1
                    if length < minL:
                        minL = length
                        minSlow = slow
                    
        if minL > len(s):
            return ""
        else:
            return s[minSlow:minSlow+minL]


# @lc code=end

