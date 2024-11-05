1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I need to construct a deep copy of the given graph from the given adjacency list
- Just itearting from left to right, I can't populate 1's neighbor list with its neighboring nodes if those are created yet
- In that case, I'll have to create the nodes first before connecting them by these lists
- To have easy access, I can use a hashmap, where key is the number and the value is a Node
- Then, I'll iterate through the adjacency list, and add their neighbors to their lists
- This can be done with the hashmap and a dfs/bfs traversal

4. Assess the space/time complexity:
- Space: O(n) for all n nodes that are explored. Already explored nodes get returned immediately
- Time: O(n) as all n nodes have to be explored

5. Optional - Give any ways you would improve your solution: