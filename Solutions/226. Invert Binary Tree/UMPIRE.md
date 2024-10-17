1. List out any clarifying questions:

2. List out 1-3 data structures/algorithms that could be useful:
- Recursion

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Breaking this down in a smaller problem, basically for any node, the right child becomes the left child and vice versa
- So, what I can do, is recursively call the function on itself for the left and right children. Then set the current node's left child as the right and vice versa. 
- Finally, I just return the node 

4. Assess the space/time complexity:
- Space: O(n), since it corresponds to the recursion stack. In the worst case where each node is on its own level, then there will be O(n) recursive calls. In the case in which each node has both children populated, then the number of calls is halved, so it ends up being O(logn)
- Time: O(n) since I need to process all n nodes and swap the children for every node

5. Optional - Give any ways you would improve your solution: