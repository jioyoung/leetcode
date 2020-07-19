#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses, prerequisites):
        courseChild = {} # course : number of pres
        coursePre = {} # course: set(childs)
        courseTake = set()
        for one in prerequisites:
            if one[0] not in courseChild:
                courseChild[one[0]] = 1
            else:
                courseChild[one[0]] +=1
            if one[1] not in coursePre:
                coursePre[one[1]] = set([one[0]])
            else:
                coursePre[one[1]].add(one[0])
        
        for i in range(numCourses):
            if i not in courseChild:
                courseTake.add(i)
        
        if not courseTake:
            return []

        ret = list(courseTake)

        while courseTake:
            take = courseTake.pop()
            if take in coursePre:
                for ichild in coursePre[take]:
                    # value is child
                    courseChild[ichild]-=1
                    if courseChild[ichild] == 0:
                        courseTake.add(ichild)
                        ret.append(ichild)
        if sum(courseChild.values())>0:
            return []

        return ret


        
# @lc code=end

