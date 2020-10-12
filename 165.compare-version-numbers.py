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
        minL = min(len1, len2)
        for i in range(minL):
            if int(arr1[i]) == int(arr2[i]):
                continue
            elif int(arr1[i]) > int(arr2[i]):
                return 1
            else:
                return -1
        if len1 == len2:
            return 0
        elif len1 > len2:
            for i in range(minL, len1):
                if int(arr1[i]) == 0:
                    continue
                else:
                    return 1
            return 0
        else:
            for i in range(minL, len2):
                if int(arr2[i]) == 0:
                    continue
                else:
                    return -1
            return 0
            
        
# @lc code=end

