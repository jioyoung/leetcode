#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses, prerequisites):
        childCourse = {}
        preCourse = {}
        for request in prerequisites:
            if request[0] not in childCourse:
                childCourse[request[0]] = 1
            else:
                childCourse[request[0]] +=1
            if request[1] not in preCourse:
                preCourse[request[1]] = set([request[0]])
            else:
                preCourse[request[1]].add(request[0])
        
        courseTake = set()
        
        for i in range(numCourses):
            if i not in childCourse:
                courseTake.add(i)
        if len(courseTake) == 0:
            return []
        ret = list(courseTake)
        
        while courseTake:
            courseLearn = courseTake.pop()
            if courseLearn in preCourse:
                for iCourse in preCourse[courseLearn]:
                    childCourse[iCourse]-=1
                    if childCourse[iCourse] == 0:
                        courseTake.add(iCourse)
                        ret.append(iCourse)
        if sum(childCourse.values()) > 0:
            return []
        else:
            return ret

# print(Solution().findOrder(2, [[1,0]]))
        
# @lc code=end

