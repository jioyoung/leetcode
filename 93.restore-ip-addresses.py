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
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        temp = []
        self.generateRes(0, s, res, temp, 0)
        #self.dfs(s, 0, "", res)
        return res
        
    def generateRes(self, start, s, res, temp, count):
        if len(s)-start > (4-count)*3:
            return
            
        if start == len(s):
            if count==4:
                res.append(''.join(temp[0:-1]))
            return



        if start > len(s) or count == 4: 
            return

        # add one 
        temp.append(s[start])
        temp.append('.')
        self.generateRes(start+1, s, res, temp, count+1)
        temp.pop()
        temp.pop()

        if s[start]=='0':
            return

        if start + 2 <= len(s):
            temp.append(s[start:start+2])
            temp.append('.')
            self.generateRes(start+2, s, res, temp, count+1)
            temp.pop()
            temp.pop()
        
        if start + 3 <= len(s) and int(s[start:start+3])<=255:
            temp.append(s[start:start+3])
            temp.append('.')
            self.generateRes(start+3, s, res, temp, count+1)
            temp.pop()
            temp.pop()


        

        
# @lc code=end

