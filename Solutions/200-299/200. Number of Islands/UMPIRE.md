1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- BFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The goal here is to iterate through each cell, and then once a cell with "1" is located, perform some traversal like BFS or DFS to locate all neighboring "1"s. All of these cells are part of one island. 
- Once an island is completely traversed, increment some count by 1
- To make sure that the same cell doesn't get considered for two seperate islands, once a "1" is seen, I replace it with a "0". 

4. Assess the space/time complexity:
- Space: O(n + m) for the number of islands, as BFS gets called n times. Then m for the queue structure as it holds m cells as once
- Time: O(m*n) as I need to traverse all cells

5. Optional - Give any ways you would improve your solution:
- In this problem, using a queue is typical for a bfs solution, but given the logic that I was using, I thought just using a stack could work. After trying it, LC seemed to give similar times. I'll look into this