#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (42.39%)
# Likes:    2060
# Dislikes: 100
# Total Accepted:    222.8K
# Total Submissions: 525.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set()
        ret = 0
        for i in range(len(nums)):
            numSet.add(nums[i])
        
        for i in range(len(nums)):
            value = nums[i]
            if (value-1) in numSet:
                continue
                # this value has been tested
                # skip
            else:
                count = 1
                while (value+1) in numSet:
                    count+=1
                    value+=1
                ret = max(count, ret)
        return ret
# @lc code=end

