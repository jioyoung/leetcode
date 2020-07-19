#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (36.43%)
# Likes:    1227
# Dislikes: 2968
# Total Accepted:    395.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        length = m+n
        for k in range(length-1,-1,-1):
            if (i>=0 and j >=0):
                if nums1[i] > nums2[j]:
                    nums1[k]=nums1[i]
                    i-=1
                else:
                    nums1[k]=nums2[j]
                    j-=1
            else:
                if j >=0:
                    nums1[k]=nums2[j]
                    j-=1
        

        

