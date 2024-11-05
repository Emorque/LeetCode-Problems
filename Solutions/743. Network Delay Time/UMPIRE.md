1. List out any clarifying questions:
- Can the graph have a cycle?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Djikstra's algorithm. Adjustment of the prims algorithm that I already know, but I deal with setting time to each edge weight and add the current weight plus next weight to my heap
- Doing so basically keeps track of the time of the current path 

4. Assess the space/time complexity:
- Space: max size of minHeap can be V^2 nodes. O(v^2)
- Time: E for the edges, v for vertices. Max number of E edges is proportional to V^2 nodes. There can be bidirectional edges
    - E * logv^2 -> 2Elogv -> Elogv since I perform heap operations e times on a heap the max size of v^2  

5. Optional - Give any ways you would improve your solution: