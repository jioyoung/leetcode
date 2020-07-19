#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.03%)
# Likes:    1427
# Dislikes: 188
# Total Accepted:    428.6K
# Total Submissions: 1M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# 普通的二分法 输出left即可

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # binary search and then output left
        # target > nums[left-i] for any i>0
        # target <=num[left]

        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left=mid+1
            else:
                right = mid-1
        return left


        # left, right = 0, len(nums)-1
        # while left<=right:
        #     mid = (left+right)//2
        #     if nums[mid] > target:
        #         right = mid-1
        #     elif nums[mid] < target:
        #         left = mid +1
        #     else:
        #         return mid
        
        # return left
        

