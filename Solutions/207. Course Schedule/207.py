from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courses = {}

        for i in range(numCourses):
            courses[i] = []
        
        for a, b in prerequisites:
            courses[a].append(b)
        
        def dfs(course) -> bool:
            if courses[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for preq in courses[course]:
                if not dfs(preq):
                    return False
            courses[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True