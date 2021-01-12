#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (42.56%)
# Likes:    2578
# Dislikes: 336
# Total Accepted:    447.6K
# Total Submissions: 1M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # the new char needs to be added to the each element in the result array, 
        if not digits:
            return []
        num_map = {
            '2':"abc", '3':"def", '4':"ghi", '5':"jkl",
            '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"
        }
        res = list(num_map[digits[0]])
        for i in range(1, len(digits)):
            temp = []
            for oneStr in res:
                for c in num_map[digits[i]]:
                    temp.append(oneStr+c)
            res = temp
        return res

