#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.21%)
# Likes:    4245
# Dislikes: 101
# Total Accepted:    353K
# Total Submissions: 835.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        dp_increase = [None]*length
        dp_len = 0
        for i in range(length):
            left = 0
            right = dp_len-1
            while left<=right:
                mid = (left+right)//2
                if dp_increase[mid]>=nums[i]:
                    right=mid-1
                else:
                    left = mid+1
            dp_increase[left] = nums[i]
            if left == dp_len:
                dp_len+=1
        return dp_len
            
        
# @lc code=end

