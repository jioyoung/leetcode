#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (39.40%)
# Likes:    2721
# Dislikes: 141
# Total Accepted:    311.4K
# Total Submissions: 767.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        [1] index 1 position is the required
        """
        # 上课
        lenPre = len(prerequisites)
        if lenPre == 0:
            return True
        courseCount = {}
        coursePre = {}
        for oneList in prerequisites:
            courseCount[oneList[0]] = courseCount.get(oneList[0], 0) + 1
            if oneList[1] not in coursePre:
                coursePre[oneList[1]] = set([oneList[0]])
            else:
                coursePre[oneList[1]].add(oneList[0])
        courseTake = set()
        for i in range(numCourses):
            if i not in courseCount:
                courseTake.add(i)
        if len(courseTake) == 0:
            return False
        while courseTake:
            courseLearn = courseTake.pop()
            if courseLearn in coursePre:
                for oneCourse in coursePre[courseLearn]:
                    courseCount[oneCourse]-=1
                    if courseCount[oneCourse] == 0:
                        courseTake.add(oneCourse)
        return False if sum(courseCount.values())>0 else True

            

# @lc code=end

