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
        # H指数 论文
        # sort from high to low
        # find the largest index that index+1 <= cite[index] 
        # return index + 1
        # 让其按被引次数从高到低排列，往下核对，
        # 直到某篇论文的序号大于该论文被引次数，那个序号减去1就是h指数
        # binary search
        # f(index) = index+1-cite(index)
        # find the largest index that f(index) <=0 

        # citations.sort(reverse = True)
        # left, right = 0, len(citations) - 1
        # while left <= right:
        #     mid = (left+right)//2
        #     if mid+1-citations[mid]<=0:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return right+1



        # sort from low to high
        # find the first index that length - index <= cite[index]
        # first index that index + cite[index] >= length
        # return length-index

        citations.sort()
        left, right = 0, len(citations)-1
        while left <= right:
            mid = (left+right)//2
            if mid + citations[mid] >= len(citations):
                right = mid -1
            else:
                left = mid + 1
        return len(citations) - left 
        


        
# @lc code=end

