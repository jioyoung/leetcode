#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses, prerequisites):
        courseCount = {}
        coursePre = {}
        for oneCourse in prerequisites:
            if oneCourse[0] not in courseCount:
                courseCount[oneCourse[0]] = 1
            else:
                courseCount[oneCourse[0]] += 1
            
            if oneCourse[1] not in coursePre:
                coursePre[oneCourse[1]] = set([oneCourse[0]])
            else:
                coursePre[oneCourse[1]].add(oneCourse[0])
        courseTake = set()
        for i in range(numCourses):
            if i not in courseCount:
                courseTake.add(i)
        if len(courseTake) == 0:
            return []
        res = list(courseTake)
        while courseTake:
            courseLearn = courseTake.pop()
            if courseLearn in coursePre:
                for oneCourse in coursePre[courseLearn]:
                    courseCount[oneCourse]-=1
                    if courseCount[oneCourse] == 0:
                        courseTake.add(oneCourse)
                        res.append(oneCourse)
        if sum(courseCount.values()) > 0:
            return []
        else: 
            return res

# print(Solution().findOrder(2, [[1,0]]))
        
# @lc code=end

