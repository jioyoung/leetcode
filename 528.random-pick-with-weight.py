#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        weight_sum = sum(self.weight)
        for i in range(len(self.weight)):
            self.weight[i] = self.weight[i] / weight_sum
        for i in range(1, len(self.weight)):
            self.weight[i] += self.weight[i-1]
        self.weight[-1] = 1

    def pickIndex(self) -> int:
        u = random.uniform(0,1)
        left, right = 0, len(self.weight)
        while left <= right:
            mid = (left+right)//2
            if self.weight[mid]>=u:
                right=mid-1
            else:
                left=mid+1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

