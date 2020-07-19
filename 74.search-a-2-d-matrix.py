#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix, target):
        n_r = len(matrix)
        if n_r == 0:
            return False
        n_c = len(matrix[0])
        if n_c == 0:
            return False
        if n_r == 1:
            if target < matrix[0][0] or target > matrix[0][n_c-1]:
                return False
            else:
                return self.search_value(matrix[0], n_c, target)
        else:
            if target < matrix[0][0] or target > matrix[n_r-1][n_c-1]:
                return False
            n_low, n_high = 0, n_r-1
            while n_low<=n_high:
                n_mid = (n_low+n_high)//2
                if matrix[n_mid][0] > target:
                    n_high = n_mid -1
                elif matrix[n_mid][0] < target:
                    n_low = n_mid + 1
                else:
                    n_low = n_mid + 1
                    break
            return self.search_value(matrix[n_low-1], n_c, target)
                
        
    def search_value(self, List, length, target):
        left, right = 0, length-1
        while left <= right:
            mid = (left+right)//2
            if List[mid] > target:
                right = mid - 1
            elif List[mid] < target:
                left = mid + 1
            else:
                return True
        return False


