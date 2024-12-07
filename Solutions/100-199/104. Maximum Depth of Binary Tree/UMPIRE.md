1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- BFS
- queue

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So the goal seems to be to get down to the lowest level on in the BT
- Therefore, I just need to traverse the BT and keep a record of every time I process a level
- I can do either BFS or DFS, but I think would be best since I'll just process each level at a time, instead of each path 

4. Assess the space/time complexity:
- Space: O(n) but it is unique in that the most amount of nodes that are in the queue at once is determined by the most amount of nodes in one level. Since nodes are popped, the queue won't reach n number of nodes in its size. It should always be less
- Time: O(n) if n is the number of nodes, since every node in the BT is processed

5. Optional - Give any ways you would improve your solution: