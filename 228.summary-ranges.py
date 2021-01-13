#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # range 总结
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        count = 1
        left = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count+=1
            else:
                if count == 1:
                    res.append(str(left))
                    left = nums[i]
                else:
                    res.append(str(left)+"->"+str(left+count-1))
                    count = 1
                    left = nums[i]
                    
        # the last element needs to be considered
        if count == 1:
            res.append(str(left))
        else:
            res.append(str(left)+"->"+str(left+count-1))
        return res


        
# @lc code=end

