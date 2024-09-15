1. Share questions you would ask to help understand the question:
- Can a course have more than 1 preq?
- Can all courses not have any preqs?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Hashmap (Likely)
- Visited set (Likely)

3. Write out in plain English what you want to do: 
- Have a visited set that gets populated with courses as we traverse with dfs
- If a course is traversed and is already in the set, then that means there is cycle, and all courses can't be completed.
  - Return []
- Have a hashmap to hold the courses and all of its prerequisites
- Perform dfs and then once a course with no preqs is reached, add it to the output list

4. Translate each sub-problem into pseudocode:
- initialize a output list, and a visited set, and accepted set
- and a hashmap

- for i in range(numCourses):
  - hashmap[i] = []

- for a, b in prerequisites:
  - hashmap[a].append(b)
  
- create dfs function(course) -> bool:
  - if course in accepted:
    - return True
  - if hashmap[course] = []:
    - output.append(course)
    - return True
  - if course in visited:
    - return False
  - visited.add(course)
  - for preq in hashmap[course]:
    - if not dfs(preq):
      - return False
  - visited.remove(course)
  - outpua.append(course) 
  - return True

- for i in range(numCourses):
  - if not dfs(i):
    - return []

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that two sets are used to one, ensure that there is no cycle in the prerequisites list, and the other ensures that already appended courses don't get processed again
- One weak area is that there is a lot of adding and removing of elements, and with dfs can make it hard to follow what is happening