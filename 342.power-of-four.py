#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1
        
# @lc code=end

