#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        isNeg = 0
        if numerator == 0:
            return "0"
        if (numerator > 0) == (denominator > 0):
            isNeg = 0
        else:
            isNeg = 1

        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator
        
        # now two values are positive
        ratio = numerator // denominator
        remain = numerator % denominator
        res = ''
        index = 0
        remain_dict = dict()
        if remain == 0:
            if isNeg:
                return "-" + str(ratio)
            else:
                return str(ratio)
        else:
            res = res + str(ratio) + '.'
            index = len(str(ratio)) + 1
            remain_dict[remain] = index
            # index is the index in the res string 
            # that corresponds to the next ratio
        while 1:
            numerator = 10*remain
            ratio = numerator// denominator
            remain = numerator % denominator
            res = res+str(ratio)
            index += 1
            if remain == 0:
                if isNeg:
                    return ("-" + res)
                else:
                    return res
            else:
                if remain in remain_dict:
                    pos = remain_dict[remain]
                    if isNeg:
                        return "-" + res[:pos] + '(' + res[pos:index] + ')'
                    else:
                        return res[:pos] + '(' + res[pos:index] + ')'
                else:
                    remain_dict[remain] = index  
# @lc code=end

