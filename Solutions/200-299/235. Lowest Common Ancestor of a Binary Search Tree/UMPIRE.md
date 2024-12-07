1. List out any clarifying questions:
- Are there duplicate nodes?
- Is p always less than q?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This problem consists of two parts
- 1. Locating the p and q nodes
- 2. Once located, I need to find that earliest parent that the two share
- If I come across an empty node or a node that is not p or q, they can essentially be ignored in part 1
- Since I am traversing down to find p and q, and then traversing back up to get the ancestor, using a dfs approach can work 
- Since it is a BST, I can use that to my advantage when tracking down the LCA
- Greater numbers are on the right subtree and the lower ones are on the left subtree

4. Assess the space/time complexity:
- Space: O(logn) since I am halving the number of nodes that I potentially explore when each iteration in my recursive stack
- Time: O(logn) for the same reason

5. Optional - Give any ways you would improve your solution: