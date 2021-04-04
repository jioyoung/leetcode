#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.checkAdditiveNumber(num, 0, [])

    def checkAdditiveNumber(self, num, start, rec_res):
        if start == len(num):
            if len(rec_res) > 2:
                return True
            else:
                return False
        lastEnd = 0
        if num[start] == '0':
            lastEnd = start + 1
        else:
            lastEnd = len(num)
        for end in range(start, lastEnd):
            if len(rec_res) < 2:
                rec_res.append(int(num[start:end+1]))
                if self.checkAdditiveNumber(num, end+1, rec_res):
                    return True
                else:
                    rec_res.pop()
            else:
                if rec_res[-1] + rec_res[-2] == int(num[start:end+1]):
                    rec_res.append(int(num[start:end+1]))
                    if self.checkAdditiveNumber(num, end+1, rec_res):
                        return True
                    else:
                        rec_res.pop()
        return False

# @lc code=end

