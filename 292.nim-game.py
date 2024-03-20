#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (56.16%)
# Likes:    576
# Dislikes: 1550
# Total Accepted:    210.2K
# Total Submissions: 374.7K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# Example:
# 
# 
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be 
# removed by your friend.
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 扔石头
        return n%4!=0
     
    #     winMap = {}
    #     return self.canIwin(n, winMap)
    
    # def canIwin(self, n, winMap):
    #     if n== 0:
    #         return False
    #     if n < 4:
    #         return True
    #     if n in winMap:
    #         return winMap[n]
        
    #     # I can get 1,2,3 stones
    #     for i in range(1, 4):
    #         if (self.canIwin(n-i-1, winMap) and self.canIwin(n-i-2, winMap) and self.canIwin(n-i-3, winMap)):
    #             winMap[n] = True
    #             return True
    #     winMap[n] = False
    #     return False
        
# @lc code=end

