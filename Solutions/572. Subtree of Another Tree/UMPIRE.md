1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- BFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- What I am thinking, is since I need to check if subRoot is a subtree or root, I'll primarily need to traverse through root
- I can do this will either DFS or BFS, so I'll just use BFS for personal perference
- Then, I can process each node, and only pause when I come across a node whose value matches the root of the subRoot tree. This means that my current node could potentially be where the subRoot fits right in
- To make this simplier, I can use a helper function as my magic function, comparing two given nodes and returning true if they are the same tree
- I'll do this and if this helper function ever returns True, I can return True from my main function
- If the queue from my BFS traversal is empty, meaning I checked every node, then I return False

4. Assess the space/time complexity:
- Space: The complexity is a bit trickey, since there are two things to consider, the BFS traversal and the helper function
    - For the BFS traversal, the size of the queue only gets as big as the number of nodes on the level with the most nodes, since popping and appending is happening
    - For the helper function, the size of the space here is only as many times the root and the subRoot and root have matching nodes. 
- Time: The overall time complexity should be O(n) for the number of nodes in the main root tree. Since each one node needs to be processed as a potential match for the root of the subRoot tree. Then you add m to become O(n + m), as a True testcase, would traverse all of the nodes in the subRoot as well (m number of nodes). m may have a multiplier if it ends up being checked multiple times

5. Optional - Give any ways you would improve your solution: