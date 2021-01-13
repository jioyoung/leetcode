#
# @lc app=leetcode id=275 lang=python
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (36.19%)
# Likes:    298
# Dislikes: 475
# Total Accepted:    96K
# Total Submissions: 265.3K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 0, 1, 3, 5, 6 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note:
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# Follow up:
# 
# 
# This is a follow up problem to H-Index, where citations is now guaranteed to
# be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
# 
# 
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # H指数
        # h_index: sort from high to low, the last one that
        # the rank <= citations[i], rank is the h_index
        
        # sort from low to high, rank = length - index
        # length - index <= cite[index]
        length = len(citations)
        left, right = 0, length - 1
        while left <= right:
            mid = (left+right)//2
            if mid+citations[mid]>=length:
                right = mid - 1
            else:
                left = mid + 1
        # if left == length, return 0
        return length -left

# @lc code=end

