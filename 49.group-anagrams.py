#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (49.60%)
# Likes:    2047
# Dislikes: 132
# Total Accepted:    404.5K
# Total Submissions: 815.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sort string as a key in the dictionary
        visit = {}
        for string in strs:
            key_str = ''.join(sorted(string))
            if key_str not in visit:
                visit[key_str] = [string]
            else:
                visit[key_str].append(string)
        return list(visit.values())

        # visit = {}
        # for string in strs:
        #     s_list = list(string)
        #     s_list.sort()
        #     s_string = ''.join(s_list)
        #     if s_string not in visit:
        #         visit[s_string] = [string]
        #     else:
        #         visit[s_string].append(string)
        # return list(visit.values())
    

# @lc code=end

