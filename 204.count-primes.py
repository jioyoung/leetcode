#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (29.89%)
# Likes:    1537
# Dislikes: 510
# Total Accepted:    302.5K
# Total Submissions: 992.8K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        count = 0
        noprime = set()
        for i in range(2, n):
            if i in noprime:
                continue
            else:
                count += 1
                j = 2
                while (j*i) < n:
                    noprime.add(j*i)
                    j+=1
        return count
# @lc code=end

