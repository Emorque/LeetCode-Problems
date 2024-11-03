1. List out any clarifying questions:
- If the tree has no nodes, do I return True?
- Are all the values distinct?

2. List out 1-3 data structures/algorithms that could be useful:
- Recursion

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This looks like a valid recursion problem, since at every node, I am asking the question of if it is a valid binary search tree
- So, I can have a default base case that returns true, and then recursively call isValidBST on the two subtrees
- Then, I'll always return a boolean back, and by utilizing "and", if even one node returns False, then the entire stack will end up returning False
- Actually wait, it is a bit more layered. Since I need to make sure that the entire subtree has nodes that are greater than or less than the current root. I may need a helper function that can help define this range

4. Assess the space/time complexity:
- Space: O(n) for the recursion stack, as I would potentially have to call helper on every node in the given BT
- Time: O(n) for similar reasoning

5. Optional - Give any ways you would improve your solution:
- There are creative solutions that don't utilize recursion but use stacks/queues. I'll explain these and why they work