#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens):
        numStack = []
        symbolSet = set(['+', '-', '*','/'])
        for token in tokens:
            if token not in symbolSet:
                numStack.append(int(token))
            else:
                val2 = numStack.pop()
                val1 = numStack.pop()
                if token == '+':
                    numStack.append(val2+val1)
                elif token == '-':
                    numStack.append(val1-val2)
                elif token == '*':
                    numStack.append(val1*val2)
                else:
                    numStack.append(int(val1/val2))
        return numStack[-1]
# @lc code=end

