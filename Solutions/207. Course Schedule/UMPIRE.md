1. Share questions you would ask to help understand the question:
- Can there be courses where there are no prerequisites?
- Can there be any negative numbers?
- Can a class have multiple prerequisites?
- Are there numCourses number of unique courses within the elements of prerequisites?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Cycle (Likely)

3. Write out in plain English what you want to do: 
- When drawing out the example, I realized that one way to check if a set of cources would return False, is if there is some cycle between courses
  - for example, a case where a course A requires course B, but at the same time, B requires A. This creates a cycle
- So now, comes to question of how to navigate through the list to see any potential cycles

- Performing DFS would work, and keeping track of visited courses would mean if a course that is in the set is traversed again, there exists some cycle, so False can be returned
- If this DFS is done for each class, and False is never returned, that means no cycle exists, so the all of the courses can be finished
- actually a hashmap would be really helpful, since there may be multiple prereqs for a class, so having it all in one place makes traversing

4. Translate each sub-problem into pseudocode:
- visited = set()
- courses = {}
- create a relationship so that courses[course] = list of prerequisites

- create dfs(course) -> bool:
  - if coruses[course] == []:
    - return True # no preqs
  - if course in visitsed:
    - return False # there is a cycle
  - visited.add(course)
  - for preq in courses[course]:
    - if not dfs(preq):
      - return False
  - courses[course] = []
  - visited.remove(course)

- for i in range(numCourses):
  - if not dfs(i):
    - return False

- return True

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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

        return True -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, through the use of courses {} and courses[course] = [], any course that can successfully be completed, it is then marked as kind of not having any preqs. So, when this course gets referenced again, True can be returned right away
- One weak area is that it may be confusing to know why the course gets removed from the set. This is because once a course can be completed, we want to return True. But there is a chance that this course will be referenced by another course as a preq, if it were kept in the set, then it would False which is what we don't want
