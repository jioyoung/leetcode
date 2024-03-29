#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    # 寻找扭曲 数组 寻找
    # Time complexity : O(N) worst case (all the same), 
    # O(\log N) (all distinct) best case, where N
    # is the length of the input array.
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                #left is sorted
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[left] > nums[mid]:
                # right is sorted
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right = mid-1
            else:
                left+=1
        return False

