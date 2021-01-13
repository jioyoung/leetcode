#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 删除 重复数组 有两个
        slow = 0
        dupCount = 1
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast-1]:
                if dupCount == 1:
                    dupCount = 2
                    slow+=1
                    nums[slow] = nums[fast]
                else:
                    # dupcount == 2
                    continue
            else:
                dupCount = 1
                slow+=1
                nums[slow] = nums[fast]
        return slow+1





