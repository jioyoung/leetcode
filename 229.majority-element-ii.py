#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (34.83%)
# Likes:    1423
# Dislikes: 159
# Total Accepted:    135.3K
# Total Submissions: 388.4K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        group1 = 0
        group2 = 1
        count1 = 0
        count2 = 0
        if not nums:
            return []
        for oneValue in nums:
            if oneValue == group1:
                count1+=1
            elif oneValue == group2:
                count2+=1
            elif count1 == 0:
                group1 = oneValue
                count1=1
            elif count2 == 0:
                group2 = oneValue
                count2=1
            else:
                count1-=1
                count2-=1
                
        count1, count2 = 0, 0
        for oneValue in nums:
            if oneValue == group1:
                count1+=1
            elif oneValue == group2:
                count2+=1
        res = []
        length = len(nums)
        if count1 > length//3:
            res.append(group1)
        if count2 > length//3:
            res.append(group2)
        return res
            
        
# @lc code=end

