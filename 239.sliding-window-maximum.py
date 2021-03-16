#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

# We scan the array from 0 to n-1, keep "promising" elements in 
# the deque. The algorithm is amortized O(n) as each element is 
# put and polled once.

# At each i, we keep "promising" elements, which are potentially 
# max number in window [i-(k-1),i] or any subsequent window. 
# This means If an element in the deque and it is out of i-(k-1), 
# we discard them. We just need to poll from the head, 
# as we are using a deque and elements are ordered as the 
# sequence in the array
# Now only those elements within [i-(k-1),i] are in the deque.
# We then discard elements smaller than a[i] from the tail. 
# This is because if a[x] <a[i] and x<i, then a[x] has no 
# chance to be the "max" in [i-(k-1),i], or any other subsequent 
# window: a[i] would always be a better candidate.

# As a result elements in the deque are ordered in both sequence 
# in array and their value. At each step the head of the deque is 
# the max element in [i-(k-1),i]
        dq = deque()
        out = []
        for i, n in enumerate(nums):
            if i >= k and dq[0] == i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                out.append(nums[dq[0]])
        return out


# @lc code=end

