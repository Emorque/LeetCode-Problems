1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Drawing an example tree that was build by going left -> right with the edges list, the first edge that causes a cycle in the tree should be what gets returned 
- So the general logic should be to build the tree with each cycle, and the edge that causes a cycle should be what gets returned 
- If you add edges to an already connected graph, then that is creating a cycle
- A way to do this is to use the logic union find
- find finds the parent node of the two given nodes
- if these parents are equal, then that means that by adding this edge, a cycle is being created
- otherwise, I can set the parent of both nodes to be the node that has the most nodes in its graph

4. Assess the space/time complexity:
- Space: O(n) for the two created lists parent and rank
- Time: O(n)

5. Optional - Give any ways you would improve your solution:
- I should study union find more. A very useful algorithm for detecting cycles in undirected graphs