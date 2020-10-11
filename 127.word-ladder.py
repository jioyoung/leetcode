#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (25.72%)
# Likes:    1931
# Dislikes: 917
# Total Accepted:    311.7K
# Total Submissions: 1.2M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordQueue = []
        alphaString = 'abcdefghijklmnopqrstuvwxyz'
        wordQueue.append(beginWord)
        visited = set([beginWord])
        isFound = False
        length=0
        while wordQueue:
            size = len(wordQueue)
            subVisit = []
            for i in range(size):
                temp = wordQueue.pop(0)
                for j in range(len(temp)):
                    part1 = temp[:j]
                    part2 = temp[j+1:]
                    for ch in alphaString:
                        if temp[j] != ch:
                            neighbour = part1 + ch + part2
                            if neighbour in wordList and neighbour not in visited:
                                subVisit.append(neighbour)
                                if neighbour == endWord:
                                    isFound = True
                                    break
                                wordQueue.append(neighbour)
                    if isFound:
                        break  
                if isFound:
                    break  
            if len(subVisit)>0:
                length+=1
            visited.update(subVisit)
            if isFound:
                length+=1
                break

        if isFound:
            return length
        else:
            return 0
             
# @lc code=end

