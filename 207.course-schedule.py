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

        nList = len(prerequisites)
        if nList == 0:
            return True
        course = dict() # record the key = couse : value = number of prerequisites
        coursePre = dict() # record the courses that are prerequisites 
                           # key = pre course: value = child course
        
        courseTake = set()
        
        for Clist in prerequisites:
            if Clist[0] not in course:
                course[Clist[0]] =  1
            else:
                course[Clist[0]] += 1
            
            if Clist[1] not in coursePre:
                coursePre[Clist[1]] = set([Clist[0]])
            else:
                coursePre[Clist[1]].add(Clist[0])
        
        for i in range(numCourses):
            if i not in course:
                courseTake.add(i)
        if not courseTake:
            return False
        
        while courseTake:
            # pop out one course, take it
            iPre = courseTake.pop()
            if iPre in coursePre:
                # it is a prerequestite
                child = coursePre[iPre] 
                for iChild in child:
                    course[iChild]-=1
                    if course[iChild] == 0:
                        courseTake.add(iChild)
        # check if there is any course that has >0 precourse
        if sum(course.values())>0:
            return False
        
        return True

            

            
            






        
# @lc code=end

