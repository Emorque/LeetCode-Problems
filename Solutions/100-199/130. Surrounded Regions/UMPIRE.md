1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Instead of focusing on all of the O cells, what if I went from the borders to the inside
- So if I come across an "O" cell in the board, I'll perform dfs or bfs and mark its region as safe in a safe set
- Then, I just have to do one pass of the board and convert and "O"s not in this set to "X"s

4. Assess the space/time complexity:
- Space: O(n) where n represents the number of "safe" cells in the board, as they are what populates the queue
- Time: O(n * m) as all cells are processed, some twice

5. Optional - Give any ways you would improve your solution:
- In my solution, I broke the bfs into its own function, but a more optimized way is to just queue append in the two first for loops and then run that queue after wards in the main function.