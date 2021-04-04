#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        sortedSet = sorted(set(s))
        nUnique = len(sortedSet)
        visited = []
        inputS = s
        while len(visited) < nUnique:
            for c in sortedSet:
                if c in visited:
                    continue
                index = inputS.index(c)
                if len(set(inputS[index:])) == nUnique - len(visited):
                    inputS = inputS[index:].replace(c, '')
                    visited.append(c)
                    break
        return ''.join(visited)


    # def removeDuplicateLetters(self, s: str) -> str:
    #     sortedSet = sorted(set(s))
    #     nUnique = len(sortedSet)
    #     return self.getRes( s, nUnique, sortedSet, [])

    # def getRes(self, s, nUnique, sortedSet, visited):
    #     if len(visited) == nUnique:
    #         return ''
    #     for c in sortedSet:
    #         if c in visited:
    #             continue
    #         tmp = s[s.index(c):]
    #         if len(set(tmp)) == (nUnique-len(visited)):
    #             visited.append(c)
    #             res =  c + self.getRes(tmp.replace(c, ''), nUnique, sortedSet, visited)
    #             visited.pop()
    #             return res


# @lc code=end

