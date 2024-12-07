1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The brute force way to do this, would be to perform dfs on each individual cell and see if can flow to both oceans
- Some time can be saved if a set of used to mark sucessful cells to reduce some repeat work
- Instead of going from cell to ocean, I can do the reverse and go from ocean to cell
- I'll mark all cells that can flow into pacific and then cells that can flow into atlantic
- If a cell can be found in both strucutres, I can add it to my result list
- Since cells can have equal heights, I'll use a visited set to not be caught in a loop

4. Assess the space/time complexity:
- Space: 
- Time: 

5. Optional - Give any ways you would improve your solution: