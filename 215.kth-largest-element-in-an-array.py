#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (49.98%)
# Likes:    2848
# Dislikes: 209
# Total Accepted:    511.1K
# Total Submissions: 983.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse = True)
        return nums[k-1]
        #return self.getKthLargest(nums, 0, len(nums)-1, k)
    
    # 选一个pivot 大的放左边 小的放右边 
    # 重复 递归

    def getKthLargest(self, nums, start, end, k):
        i = start
        pivot = nums[end]
        if start == end:
            return nums[start]
        for j in range(start, end):
            # j is from start to end-1 !!!!!!!!!
            if nums[j]>=pivot:
                # exchange i,j
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        #交换i 和 end ; after that, ith index is pivot now
        nums[i], nums[end] = nums[end], nums[i]

        #idx start to i-1 are all >= pivot
        count = i-start+1
        if count == k:
            return pivot
        elif count < k:
            # 在右边
            return self.getKthLargest(nums, i+1, end, k-count)
        else:
            # 在左边 ith idx is pivot it can be ignored
            return self.getKthLargest(nums, start, i-1, k)
        

        
# @lc code=end

