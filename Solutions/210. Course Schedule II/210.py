from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            preq[a].append(b)
        
        visited = set()
        schedule = []

        def validCourse(course) -> bool:
            if preq[course] == []: 
                if course not in visited:
                    visited.add(course)
                    schedule.append(course)
                return True
            if course in visited:
                return False
            
            visited.add(course)

            for p in preq[course]:
                if validCourse(p) == False:
                    return False
            schedule.append(course)
            preq[course] = []
            return True
            
        for i in range(numCourses):
            if validCourse(i) == False:
                return []
        return schedule