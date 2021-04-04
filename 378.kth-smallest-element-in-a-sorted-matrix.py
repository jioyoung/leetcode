#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = []
        for i in range(n):
            heapq.heappush(h, (matrix[i][0], i, 0))
        for i in range(k-1):
            value, iRow, iCol = heapq.heappop(h)
            if iCol < n-1:
                heapq.heappush(h, (matrix[iRow][iCol+1], iRow, iCol+1))

        return heapq.heappop(h)[0]
        
# @lc code=end

