#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # Solution one two pointer O(n)
        # left = right = 0
        # subsum = 0
        # length = len(nums)
        # res = length + 1
        # while right < length:
        #     subsum += nums[right]
        #     right+=1
        #     while subsum >= s:
        #         res = min(res, right-left)
        #         subsum-=nums[left]
        #         left+=1
        # if res == length+1:
        #     return 0
        # else:
        #     return res

        # solution two: O(nlogn)
        length = len(nums)
        if length == 0:
            return 0
        subsum = [None]*length
        subsum[0] = nums[0]
        res = length+1
        for i in range(1, length):
            subsum[i] = subsum[i-1] + nums[i]
        
        # for starting i, find first j such that
        # subsum[j]-subsum[i] + nums[i] >= s
        # subsum[j] >= s-nums[i]+subsum[i]
        for i in range(length):
            target = s - nums[i] + subsum[i]
            left, right = i, length-1
            while left <= right:
                mid = (left+right)//2
                if subsum[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            if left < length:
                res = min(res, left-i+1)
        return res if res <= length else 0



# @lc code=end

