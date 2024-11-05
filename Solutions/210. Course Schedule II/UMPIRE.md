1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Very similiar to 1 and I think I only need to make a few minor adjustments
- Instead of return False if valid Course returns False, just return an empty array
- And then, whenever I am just about to return True in the inner validCourse function, I just append that course to my schedule list, as it should be a course that can be taken at that order
- Thanks to the recursion stack, only courses that are be taken the soonest are fully executed first

4. Assess the space/time complexity:
- Space: O(n) for the preq list, visited set, schedule list, and calls to validCourse
- Time: O(n) for the same things

5. Optional - Give any ways you would improve your solution: