#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#

# @lc code=start
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        validTimes = []
        self.getPermuteUnique(arr, validTimes, [], [])
        if not validTimes:
            return ""
        validTimes.sort(key = lambda x:(x[0], x[1]))
        if len(validTimes) == 1: 
            maxTime = validTimes[-1]
        else:
            if validTimes[-1][0]==24:
                maxTime = validTimes[-2]
            else:
                maxTime = validTimes[-1]
        value = maxTime[0]
        res = ''
        if value<10:
            res += ('0' + str(value))
        else:
            res += str(value)
        res+=':'
        value = maxTime[1]
        if value<10:
            res += ('0' + str(value))
        else:
            res += str(value)
        return res

    def getPermuteUnique(self, nums, res, rec_res, rec_idx):
        if len(rec_res) == len(nums):
            valueStr = ''.join(rec_res)
            value1 = int(valueStr[:2])
            value2 = int(valueStr[2:])
            if value1 <= 24 and value2 < 60:
                if value1 == 24:
                    if value2 == 0:
                        res.append([value1, value2])
                else:
                    res.append([value1, value2])
            return

        for i in range(len(nums)):
            if i in rec_idx:
                continue
            if i > 0 and i-1 not in rec_idx and nums[i-1] == nums[i]:
                continue
            rec_res.append(str(nums[i]))
            rec_idx.append(i)
            self.getPermuteUnique(nums, res, rec_res, rec_idx)
            rec_res.pop()
            rec_idx.pop()
        return
# @lc code=end

