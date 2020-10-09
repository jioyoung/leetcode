#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens):
        tokenStack = []
        for t in tokens:
            if t.isdigit():
                tokenStack.append(int(t))
            elif len(t)>1 and t[0].isdigit() == False:
                tokenStack.append(-int(t[1:]))
            else:
                v2 = tokenStack.pop()
                v1 = tokenStack.pop()
                if t == '+':
                    tokenStack.append(v1+v2)
                elif t=='-':
                    tokenStack.append(v1-v2)
                elif t=='*':
                    tokenStack.append(v1*v2)
                else:
                    tokenStack.append(int(v1/v2))
        return tokenStack.pop()

# @lc code=end

