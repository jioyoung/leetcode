#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primesIdx = [0 for i in range(len(primes))]
        if n == 1:
            return 1
        uglyArr = [None] * n
        uglyArr[0] = 1
        candidates = [0 for i in range(len(primes))]
        for i in range(1, n):
            minValue = float('inf')
            for j in range(len(primes)):
                newValue = uglyArr[primesIdx[j]]*primes[j]
                candidates[j] = newValue
                if newValue < minValue:
                    minValue = newValue
            for j in range(len(primes)):
                if candidates[j] == minValue:
                    primesIdx[j]+=1
            uglyArr[i] = minValue
        return uglyArr[-1]




# @lc code=end

