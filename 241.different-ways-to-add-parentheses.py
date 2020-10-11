#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def calculate(self, l_value, op, r_value):
        if op == '+':
            return l_value + r_value
        elif op == '-':
            return l_value - r_value
        else:
            return l_value * r_value


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # dynamic programming
        num = 0
        operList = []
        numList = []
        for i in range(len(input)):
            if not input[i].isdigit():
                numList.append(num)
                operList.append(input[i])
                num = 0
            else:
                num = num * 10 + int(input[i])
        # the last number needs to be added
        numList.append(num)
        numN = len(numList)
        if numN == 1:
            return numList
        
        result = [[[] for _ in range(numN)]  for __ in range(numN)]
        for i in range(numN):
            result[i][i].append(numList[i])

        # result[1][3] 就代表第一个数字 3 到第三个数字 5 范围内的表达式 3 - 4 * 5 的所有解。

        for n in range(2, numN+1):
            for i in range(numN-n+1):
                j = i + n -1
                for k in range(i, j):
                    # two parts the first is
                    for l_value in result[i][k]:
                        for r_value in result[k+1][j]:
                            result[i][j].append(self.calculate(l_value, operList[k], r_value)) 

        return result[0][-1]  
        
# @lc code=end

