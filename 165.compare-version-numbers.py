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
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        minL = min(arr1_len, arr2_len)
        for i in range(minL):
            if int(arr1[i]) == int(arr2[i]):
                continue
            elif int(arr1[i]) > int(arr2[i]):
                return 1
            else:
                return -1
        if arr1_len == arr2_len:
            return 0
        if arr1_len < arr2_len:
            for i in range(minL, arr2_len):
                if int(arr2[i])>0:
                    return -1
                else:
                    continue
            return 0
        else:
            for i in range(minL, arr1_len):
                if int(arr1[i]) > 0:
                    return 1

                else:
                    continue
            return 0
            
        
# @lc code=end

