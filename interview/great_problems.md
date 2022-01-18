

#### 计算器 字符串
```python
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
```

#### 加括号 计算器
```python
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
        # dynamic programming 括号 parenthesis 加括号
        # 计算器
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
        # 可以重复
        # n is the number of the nums from 2 to numN
        for n in range(2, numN+1):
            for i in range(numN-n+1):
                j = i + n -1
                for k in range(i, j):
                    # two parts the first is
                    for l_value in result[i][k]:
                        for r_value in result[k+1][j]:
                            result[i][j].append(self.calculate(l_value, operList[k], r_value)) 

        return result[0][-1]  
```


#### sliding window maximum (deque)
```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

# We scan the array from 0 to n-1, keep "promising" elements in 
# the deque. The algorithm is amortized O(n) as each element is 
# put and polled once.

# At each i, we keep "promising" elements, which are potentially 
# max number in window [i-(k-1),i] or any subsequent window. 
# This means If an element in the deque and it is out of i-(k-1), 
# we discard them. We just need to poll from the head, 
# as we are using a deque and elements are ordered as the 
# sequence in the array
# Now only those elements within [i-(k-1),i] are in the deque.
# We then discard elements smaller than a[i] from the tail. 
# This is because if a[x] <a[i] and x<i, then a[x] has no 
# chance to be the "max" in [i-(k-1),i], or any other subsequent 
# window: a[i] would always be a better candidate.

# As a result elements in the deque are ordered in both sequence 
# in array and their value. At each step the head of the deque is 
# the max element in [i-(k-1),i]
        dq = deque()
        out = []
        for i, n in enumerate(nums):
            if i >= k and dq[0] == i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                out.append(nums[dq[0]])
        return out
```

#### 最大正方形
```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 最大面积 用 dp[i][j] 表示以 matrix[i][j] 为右下角正方形的最大边长
        # dynamic programming
        # if max_edge[i][j]==1:
        # max_edge[i][j] = min(max_edge[i-1][j-1],max_edge[i-1][j],max_edge[i][j-1]) + 1
        nRow = len(matrix)
        if nRow == 0:
            return 0
        nCol = len(matrix[0])
        if nRow == 1:
            for i in range(nCol):
                if matrix[0][i] == '1':
                    return 1
            return 0
        if nCol == 1:
            for i in range(nRow):
                if matrix[i][0] == '1':
                    return 1
            return 0
        pre_top_left = 0
        # 下边是空间复杂度优化的代码，最关键的是用 pre_top_left 保存了左上角的值
        max_edge = 0
        row_dp = [0]*(nCol+1)
        for i in range(1, nRow+1):
            for j in range(1, nCol+1):
                temp = row_dp[j]
                if matrix[i-1][j-1]=='0':
                    row_dp[j] = 0
                else:
                    row_dp[j] = min(row_dp[j-1], row_dp[j], pre_top_left) + 1
                    max_edge = max(max_edge, row_dp[j])
                pre_top_left = temp
        return max_edge**2

    # 代码的话，使用个技巧，那就是行和列多申请一行，这样的话第一行和第一列的情况就不需要单独考虑了。
    # int rows = matrix.length;
    # if (rows == 0) {
    #     return 0;
    # }
    # int cols = matrix[0].length;
    # int[][] dp = new int[rows + 1][cols + 1];
    # int maxSide = 0;
    # for (int i = 1; i <= rows; i++) {
    #     for (int j = 1; j <= cols; j++) {
    #         //因为多申请了一行一列，所以这里下标要减 1
    #         if (matrix[i - 1][j - 1] == '0') {
    #             dp[i][j] = 0;
    #         } else {
    #             dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
    #             maxSide = Math.max(dp[i][j], maxSide);
    #         }
    #     }
    # }
    # return maxSide * maxSide;
```

#### 分桶 重复
```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # seperate the num into different bucket
        # 分桶 bucket 有条件重复
        if t< 0:
            return False
        width = t+1
        num_dict = dict()
        for i in range(len(nums)):
            value = nums[i]//width
            if value in num_dict:
                return True
            if (value-1) in num_dict and abs(num_dict[value-1]-nums[i])<width:
                return True
            if (value+1) in num_dict and abs(num_dict[value+1]-nums[i])<width:
                return True
            num_dict[value] = nums[i]
            if i >=k:
                del num_dict[nums[i-k]//width]
        return False
```

#### 字符串 最大数
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # sort the array based on a scheme
        # bubble sort with flag
        # 冒泡法 组成 最大 数 字符串 组合 最大数

        for i in range(len(nums)):
            nums[i] = str(nums[i])
        end = len(nums)
        while end:
            oldEnd = end
            end = 0
            for i in range(1, oldEnd):
                if self.compareTwoString(nums[i-1], nums[i]):
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    end = i
        if int(nums[0]) == 0:
            return '0'
        return ''.join(nums)

    def compareTwoString(self, s1, s2):
        if s1+s2 < s2+s1:
            return 1
        else:
            return 0 
```

#### peak element
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 山峰 峰值 peak
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
```