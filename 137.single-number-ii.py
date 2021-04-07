#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (47.21%)
# Likes:    1168
# Dislikes: 302
# Total Accepted:    193.9K
# Total Submissions: 401.2K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 出现一次
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0)+1
        for key, val in nums_dict.items():
            if val == 1:
                return key

        # ones   代表第 ith 位只出现一次的掩码变量
        # twos  代表第 ith 位只出现两次次的掩码变量
        # threes  代表第 ith 位只出现三次的掩码变量
        #假设现在有一个数字1，更新 one 的方法就是 ‘亦或’ 这个1，则 one 就变成了1，
        # 而 two 的更新方法是用上一个状态下的 one 去 ‘与’ 上数字1，然后 ‘或’ 上这个结果，
        # 这样假如之前 one 是1，那么此时 two 也会变成1，这 make sense，
        # 因为说明是当前位遇到两个1了；反之如果之前 one 是0，那么现在 two 也就是0。
        # 注意更新的顺序是先更新 two，再更新 one，不理解的话只要带个只有一个数字1的输入数组看一下
        # 就不难理解了。然后更新 three，如果此时 one 和 two 都是1了，由于先更新的 two，
        # 再更新的 one，two 为1，说明此时至少有两个数字1了，而此时 one 为1，说明了此时
        # 已经有了三个数字1，这块要仔细想清楚，因为 one 是要 ‘亦或’ 一个1的，值能为1，
        # 说明之前 one 为0，实际情况是，当第二个1来的时候，two 先更新为1，此时 one 再更新为0，
        # 下面 three 就是0了，那么 ‘与’ 上three 的相反数1不会改变 one 和 two 的值；
        # 那么当第三个1来的时候，two 还是1，此时 one 就更新为1了，那么 three 就更新为1了，
        # 此时就要清空 one 和 two 了，让它们 ‘与’ 上 three 的相反数0即可，
        # 最终结果将会保存在 one 中，参见代码如下：

        # one, two = 0, 0
        # for x in nums:
        #     one, two, three = one ^ x, two | (one & x), two & x
        #     one, two = one & ~three, two & ~three
        # return one

# @lc code=end

