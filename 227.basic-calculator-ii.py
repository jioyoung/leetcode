#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        # delete the space at the begining and end
        # 计算器
        s = s.strip()
        if not s:
            return 0
        sign = '+'
        num = 0
        valueStack = []
        for c in s:
            if c.isdigit() == True:
                num = 10*num + ord(c) - ord('0')
            elif c == ' ':
                continue
            else:
                self.pushtoStack(sign, num, valueStack)
                num = 0
                sign = c
        # the last chars are always digits since strip has been used
        # add the last number to the stack
        self.pushtoStack(sign, num, valueStack)
        
        return sum(valueStack)
            

    def pushtoStack(self, c, num, stackList):
        if c == '+':
            stackList.append(num)
        elif c == '-':
            stackList.append(-num)
        elif c == '*':
            stackList[-1] = stackList[-1]*num
        else:
            stackList[-1] = int(stackList[-1]/num)



        
        
# @lc code=end

