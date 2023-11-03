#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2*10**9
        while left <= right:
            mid = (left+right)//2
            if self.count_factor(mid, a, b, c) >= n:
                right = mid - 1 
            else:
                left = mid + 1
        return left

    
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b,a)
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a*b/self.gcd(a,b)
    
    def count_factor(self, n, a, b, c):
        setA = n // a
        setB = n // b
        setC = n // c
        lcm_ab = self.lcm(a,b)
        setAB = n//lcm_ab
        setAC = n//(self.lcm(a,c))
        setBC = n//(self.lcm(b,c))
        setABC = n//self.lcm(c, lcm_ab)
        return setA+setB+setC-setAB-setBC-setAC+setABC


# @lc code=end

