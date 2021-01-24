#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (54.27%)
# Likes:    2184
# Dislikes: 186
# Total Accepted:    468.1K
# Total Submissions: 851.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):

        '''
        投票法。。就是省空间而已 
        遇到自己数量就加一 不然就减一
        数量变成零 就新的一组
        众数
        '''
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                count+=1
            else:
                if count == 0:
                    major = nums[i]
                    count = 1
                else:
                    count-=1
        return major

        """
        :type nums: List[int]
        :rtype: int
        hashMap最简单，，
        投票法 group转换

        if len(nums)==1:
            return nums[0]
        numDic = {}
        thrs = len(nums)//2
        for i in range(len(nums)):
            oneNum = nums[i]
            if oneNum in numDic:
                numDic[oneNum]+=1
                if numDic[oneNum]>thrs:
                    return oneNum
            else:
                numDic[oneNum]=1
        """
        
# @lc code=end

