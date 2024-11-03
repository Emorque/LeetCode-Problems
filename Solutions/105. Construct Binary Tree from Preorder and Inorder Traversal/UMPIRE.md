1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Recursion
- Splicing

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I know that preorder is: root, left, right; and inorder is left, root, right
- In that case, that means that I can always locate the root as the first node in the preorder list.
- Then for that node in the inorder list, is left subtree will be all the nodes to the left of it and the right subtree will be all the nodes to the right of it 

4. Assess the space/time complexity:
- Space: O(n) as I need to recursively call this on every element in the lists, as they should both have n elements
- Time: O(n) for the same reasoning

5. Optional - Give any ways you would improve your solution:
- Instead of using a for loop to locate the root in the inorder array, I could have used index()