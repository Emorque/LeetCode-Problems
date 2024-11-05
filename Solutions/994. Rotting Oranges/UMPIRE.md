1. List out any clarifying questions:
- Can there be more than one rotten orange?

2. List out 1-3 data structures/algorithms that could be useful:
- BFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This looks like a problem with an intuitive bfs approach
- I can use a queue, and then for every loop within the queue, I'll process depending on the number of oranges at the start, and then after that, increment my timer by 1
- This way I am processing these oranges by the minute instead of individually

4. Assess the space/time complexity:
- Space: O(n*m) in that case that all cells have to be explored
- Time: O(n*m) as all cells have to be explored 

5. Optional - Give any ways you would improve your solution: