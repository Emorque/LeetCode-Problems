1. List out any clarifying questions:

2. List out 1-3 data structures/algorithms that could be useful:
- BFS, DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- For this question, it looks like I can just just bfs/dfs traversal to find all the cells in an island. Then, I can return some area everytime I encounter an island. 
- Once the area is returned, I'll compare it with the current area that I have and record the larger area

4. Assess the space/time complexity:
- Space: O(i * c) where i is the number of islands and c is the average size of the islands. (BFS)
- Time: O(n*m) as I need to process all cells at least once

5. Optional - Give any ways you would improve your solution: