#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.20%)
# Likes:    2346
# Dislikes: 183
# Total Accepted:    380.2K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # first sort and then merge 
        if len(intervals)<=1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                if result[-1][1]<=intervals[i][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result
    



        # if len(intervals)<=1:
        #     return intervals
        # intervals.sort(key = lambda x:x[0])
        # i = 1
        # while 1:
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         if intervals[i][1]>intervals[i-1][1]:
        #             intervals[i-1][1] = intervals[i][1]
        #         del intervals[i]
        #     else:
        #         i+=1
        #     if i == len(intervals):
        #         return intervals




        
# @lc code=end

