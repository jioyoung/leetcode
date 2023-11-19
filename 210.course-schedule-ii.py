#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 上课
        if not prerequisites:
            return list(range(numCourses))
        preCourseCount = {}
        childCourse = {}
        for oneList in prerequisites:
            preCourseCount[oneList[0]] = preCourseCount.get(oneList[0], 0) + 1
            if oneList[1] not in childCourse:
                childCourse[oneList[1]] = set([oneList[0]])
            else:
                childCourse[oneList[1]].add(oneList[0])
        
        courseCanTake = [i for i in range(numCourses) if i not in preCourseCount]
        res = list(courseCanTake)
        while courseCanTake:
            oneCourse = courseCanTake.pop()
            if oneCourse in childCourse:
                for oneChild in childCourse[oneCourse]:
                    preCourseCount[oneChild]-=1
                    if preCourseCount[oneChild] == 0:
                        courseCanTake.append(oneChild)
                        res.append(oneChild)
        if sum(preCourseCount.values()) > 0:
            return []
        else:
            return res



# print(Solution().findOrder(2, [[1,0]]))
        
# @lc code=end

