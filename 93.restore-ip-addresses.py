#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.52%)
# Likes:    817
# Dislikes: 344
# Total Accepted:    155K
# Total Submissions: 475.3K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#

# @lc code=start
class Solution(object):
    # ip 地址 ip地址 
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.getIpAddresses(s, 0, res, [], 0)
        return res
        
    def getIpAddresses(self, s, index, res, rec_res, count):
        if index == len(s):
            if count == 4:
                res.append(''.join(rec_res)[:-1])
            return
        
        # stopping condition 2
        if len(s) - index > (4-count)*3:
            return 
        
        # stopping condition 3
        if count >= 4:
            return 
        
        
        rec_res.append(s[index]+'.')
        self.getIpAddresses(s, index+1, res, rec_res, count+1)
        rec_res.pop()
        
        if s[index] == '0':
            return # 0 can not be used as a head of a string longer than 1
        
        if index + 1 < len(s):
            rec_res.append(s[index:index+2]+'.')
            self.getIpAddresses(s, index+2, res, rec_res, count+1)
            rec_res.pop()
        
        if index +2 < len(s) and int(s[index:index+3])<=255:
            rec_res.append(s[index:index+3]+'.')
            self.getIpAddresses(s, index+3, res, rec_res, count+1)
            rec_res.pop()            
            
        return   
# @lc code=end

