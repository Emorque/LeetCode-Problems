1. List out any clarifying questions:
- So then in any Tree with a root, the root will always be a good node?
- Are there duplicate values?

2. List out 1-3 data structures/algorithms that could be useful:
- Recursion

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since each nodes's path from the root to itself is unique, using a recursive helper function will be pretty intuitive
- I'll have some good count int 
- Then in the helper function, I'll pass in a node and the current greatest value
- Then, depending on the node's value, when I go to recursively call the helper on the children node, I'll change what I send as the greatest value
- Since I am using a recursive approach, these greatest values will stay unique to their path
- The same still works for an iterative approach with a queue, which I will apply the same logic too

4. Assess the space/time complexity:
- Space: O(m) where m represents the most number of nodes present in a single level of the given BT
- Time: O(n) where n represents the number of nodes in the BT

5. Optional - Give any ways you would improve your solution:
- Not neccessarily better, but the solution could also be done as described as a dfs solution