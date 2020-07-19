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
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.getidxlarge(nums1, nums2, total_len//2) 
        else:
            return 0.5*self.getidxlarge(nums1, nums2, total_len//2-1) + 0.5*self.getidxlarge(nums1, nums2, total_len//2) 


    def getidxlarge(self, nums1, nums2, idx):
        if not nums1:
            return nums2[idx]
        if not nums2:
            return nums1[idx]
        iMid_1 = len(nums1)//2
        iMid_2 = len(nums2)//2
        mid_1 = nums1[iMid_1]
        mid_2 = nums2[iMid_2]
        if (iMid_1+iMid_2) >= idx:
            if mid_1 > mid_2:
                return self.getidxlarge(nums1[:iMid_1], nums2, idx)
            else:
                return self.getidxlarge(nums1, nums2[:iMid_2], idx)
        else:
            if mid_1 > mid_2:
                return self.getidxlarge(nums1, nums2[iMid_2+1:], idx-iMid_2-1)
            else:
                return self.getidxlarge(nums1[iMid_1+1:], nums2, idx-iMid_1-1)


    #     tot_len = len(nums1) + len(nums2)
    #     K = tot_len // 2
    #     if tot_len % 2 == 0:
    #         return 0.5*(self.findKthlargest(nums1, nums2,K-1)+self.findKthlargest(nums1, nums2, K))
    #     else:
    #         return self.findKthlargest(nums1, nums2,K)
    
    # def findKthlargest(self, nums1, nums2, K):
    #     if not nums1:
    #         return nums2[K]
    #     if not nums2:
    #         return nums1[K]
    #     iMid_1 = len(nums1)//2
    #     iMid_2 = len(nums2)//2
    #     Mid_1 = nums1[iMid_1]
    #     Mid_2 = nums2[iMid_2]
    #     if iMid_1+iMid_2 >= K:
    #         if Mid_1 > Mid_2:
    #             return self.findKthlargest(nums1[:iMid_1], nums2, K)
    #         else:
    #             return self.findKthlargest(nums1, nums2[:iMid_2], K)
    #     else:
    #         if Mid_1 > Mid_2:
    #             return self.findKthlargest(nums1, nums2[iMid_2+1:], K-iMid_2-1)
    #         else:
    #             return self.findKthlargest(nums1[iMid_1+1:], nums2, K-iMid_1-1)
        

