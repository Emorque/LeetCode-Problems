1. List out any clarifying questions:
- Can there be duplicate values?

2. List out 1-3 data structures/algorithms that could be useful:
- stack

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Given that it is a BST, I feel like that is a very important detail
- This means that if printed in inorder, the nodes would be in ascending order
- The leftmost node would be the smallest node
- So if I were to start at the smallest node, and if k was not 1, I would need to traverse back up a bit
- so I would go back up to the parent node, and then the right subtree and then the left most node here
- In that case, I can iterate to the leftmost node, keeping track of my parent nodes
- Then, I'll keep itearting from left, current, right, until I find my kth node

4. Assess the space/time complexity:
- Space: O(n) as in the worst case of needing to constain all n nodes if all nodes are on node.left
- Time: O(n) as in that same case, all n nodes would have to be explored

5. Optional - Give any ways you would improve your solution: