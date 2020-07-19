#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (35.36%)
# Likes:    554
# Dislikes: 939
# Total Accepted:    146.3K
# Total Submissions: 413.9K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # citations.sort()
        # n = 1
        # for i in range(len(citations)-1, -1, -1):
        #     if citations[i]>=n:
        #         n+=1
        #     else:
        #         break
        # return n-1
        citations.sort()
        length = len(citations)
        left = 0
        right = length-1
        # binary search for the first index that cite[i]>=length-i
        # or cite[i] + i >= length
        # length - i is the h-index
        while left<=right:
            mid = (left+right)//2
            if citations[mid]+mid < length:
                left = mid+1
            else:
                right=mid-1
        return length - left
        
# @lc code=end

