from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = [[] for i in range(numCourses)]
        
        for a, b in prerequisites:
            preq[a].append(b)
        
        visited = set()
        
        def validCourse(course) -> bool:
            if preq[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)

            for p in preq[course]:
                if validCourse(p) == False:
                    return False
            preq[course] = []
            return True
            
        for i in range(numCourses):
            if validCourse(i) == False:
                return False

        # print(preq)

        return True