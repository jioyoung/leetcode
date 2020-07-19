#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <=2:
            return length
        i,j=1,1
        dup_num=1
        for i in range(1, length):
            if nums[i]==nums[i-1]:
                if dup_num==2:
                    continue
                else:
                    nums[j]=nums[i]
                    j+=1
                    dup_num+=1
            else:
                nums[j]=nums[i]
                j+=1
                dup_num=1
        return j


