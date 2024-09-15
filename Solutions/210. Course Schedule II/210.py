from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        visited, accepted = set(), set()
        courses = {}

        for i in range(numCourses):
            courses[i] = []

        for a, b in prerequisites:
            courses[a].append(b)
        
        def dfs(course) -> bool:
            if course in accepted:
                return True
            if courses[course] == []:
                output.append(course)
                accepted.add(course)
                return True
            if course in visited:
                return False
            visited.add(course)
            
            for preq in courses[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            output.append(course)
            accepted.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output