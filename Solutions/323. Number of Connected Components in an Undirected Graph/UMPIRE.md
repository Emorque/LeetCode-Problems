1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Union Find

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- If two components weren't connected before, decrement n by 1
- I can do this logic with the help of union find. Find will locate the main parent node of the given node, and if these parents of a and b are equal, then I know that the graphs are already connected
- If they aren't, I'll perform the union logic and also decrement n by 1 
- After iterating through all the edges, I'll return n 

4. Assess the space/time complexity:
- Space: O(n) for two arrays
- Time: O(len(edges) * n) -> n for the finds

5. Optional - Give any ways you would improve your solution: