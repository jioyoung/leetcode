#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (26.38%)
# Likes:    4324
# Dislikes: 577
# Total Accepted:    437.5K
# Total Submissions: 1.7M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # divide and conqur
        # do not forget the situation that one list is empty in the recursion
        totalN = len(nums1) + len(nums2)
        if totalN % 2 == 0:
            return (self.getidxoftwoarr(nums1, nums2, totalN//2-1) * 0.5 + 
                self.getidxoftwoarr(nums1, nums2, totalN//2) * 0.5)
        else:
            return self.getidxoftwoarr(nums1, nums2, totalN//2)
        
    def getidxoftwoarr(self, nums1, nums2, idx):
        if not nums1:
            return nums2[idx]
        if not nums2:
            return nums1[idx]
        mid_idx1 = len(nums1)//2
        mid_idx2 = len(nums2)//2
        if mid_idx1 + mid_idx2 >= idx:
            # mid_idx1+mid_idx2+2 > idx+1
            # the larger part of the array that has larger median can be ignored
            if nums1[mid_idx1] >= nums2[mid_idx2]:
                return self.getidxoftwoarr(nums1[:mid_idx1], nums2, idx)
            else:
                return self.getidxoftwoarr(nums1, nums2[:mid_idx2], idx)
        else:
            # mid_idx1+mid_idx2+2 <= idx+1
            # the smaller part of the array that has smaller mdedian can be ignored
            if nums1[mid_idx1] >= nums2[mid_idx2]:
                return self.getidxoftwoarr(nums1, nums2[mid_idx2+1:], idx-mid_idx2-1)
            else:
                return self.getidxoftwoarr(nums1[mid_idx1+1:], nums2, idx-mid_idx1-1) 
        # for both situations, the ignored part includes the median boundary
