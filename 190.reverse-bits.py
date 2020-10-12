#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        string =bin(n)[2:]
        length = len(string)
        if length < 32:
            string = (32-length)*'0'+string
        return int(string[::-1], 2)
# @lc code=end

