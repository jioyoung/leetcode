#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals, newInterval):
        # 区间 合并 插入
        # interval
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        i = 0
        j = 0
        res = []
        while i < len(intervals) or j < 1:
            if i < len(intervals) and j < 1:
                if intervals[i][0] <= newInterval[0]:
                    candidate = intervals[i]
                    i+=1
                else:
                    candidate = newInterval
                    j+=1
            elif i < len(intervals):
                candidate = intervals[i]
                i+=1
            else:
                candidate = newInterval
                j+=1
            if not res:
                res.append(candidate)
            else:
                if res[-1][1] < candidate[0]:
                    res.append(candidate)
                else:
                    res[-1][1] = max(res[-1][1], candidate[1])
        return res

