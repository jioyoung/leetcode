#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        len1 = len(arr1)
        len2 = len(arr2)
        length = min(len1, len2)
        for i in range(length):
            arr1[i] = arr1[i].lstrip('0')
            if arr1[i]:
                val1 = int(arr1[i])
            else:
                val1=0
            arr2[i] = arr2[i].lstrip('0')
            if arr2[i]:
                val2 = int(arr2[i])
            else:
                val2 = 0
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
            else:
                continue
        if len1 == len2:
            return 0
        elif len1 > len2:
            for i in range(length, len1):
                arr1[i] = arr1[i].lstrip('0')
                if arr1[i]:
                    val = int(arr1[i])
                else:
                    val=0
                if val > 0:
                    return 1
            return 0
        else:
            for i in range(length, len2):
                arr2[i] = arr2[i].lstrip('0')
                if arr2[i]:
                    val = int(arr2[i])
                else:
                    val=0
                if val > 0:
                    return -1
            return 0
            
        
# @lc code=end

