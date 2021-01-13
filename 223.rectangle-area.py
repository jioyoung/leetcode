#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    # 面积
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s1 = (C-A)*(D-B)
        s2 = (G-E)*(H-F)
        top = min(D, H)
        bottom = max(F, B)
        left = max(E,A)
        right = min(C, G)
        if right > left and top > bottom:
            s3 = (right-left)*(top-bottom)
        else:
            s3 = 0
        return s1+s2-s3
# @lc code=end

