#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (35.15%)
# Likes:    963
# Dislikes: 321
# Total Accepted:    163.7K
# Total Submissions: 463.3K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1.
# 
# Note:
# 
# 
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
# 
# 
# Example 1:
# 
# 
# Input: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 
# Output: 3
# 
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
# 
# 
# Example 2:
# 
# 
# Input: 
# gas  = [2,3,4]
# cost = [3,4,3]
# 
# Output: -1
# 
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
# 
# 
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #加油站
        '''
        加油站
        当考虑 i 能到达的最远的时候,假设是 j。
        那么 i + 1 到 j 之间的节点是不是就都不可能绕一圈了？
        假设 i + 1 的节点能绕一圈,那么就意味着从 i + 1 开始一定能到达 j + 1。
        又因为从 i 能到达 i + 1,所以从 i 也能到达 j + 1。
        但事实上,i 最远到达 j 。产生矛盾,所以 i + 1 的节点一定不能绕一圈。同理,其他的也是一样的证明。
        所以下一次的 i 我们不需要从 i + 1 开始考虑,直接从 j + 1 开始考虑即可。
        还有一种情况,就是因为到达末尾的时候,会回到 0。

        如果对于下边的情况。

        '''
        if sum(gas) < sum(cost):
            return -1
        remain = gas[0] - cost[0]
        loc = 0
        for i in range(1, len(cost)):
            if remain < 0:
                remain = gas[i] - cost[i]
                loc = i
            else:
                remain += (gas[i]-cost[i])
        return loc



# @lc code=end

