1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Because I know that I have numCourses, which gives me a range to work with. I have a courses that I can verify
- As for the preq list, I can create a relationship with a list of length numCourses, making the indexes the course and the value a list of preqs
- Create a helper function that checks each course and returns True if it can be completed
- Use a set to make sure Im not in a loop
- If a course has an empty list, it can be completed 
- If I end up in a loop, than I can return False as there are classes that need to be completed to do the other

4. Assess the space/time complexity:
- Space: O(n) for the preq list, has a length numCourses. Same for the visited set and validCourse recursive stack
- Time: O(n) for the same things listed above

5. Optional - Give any ways you would improve your solution: