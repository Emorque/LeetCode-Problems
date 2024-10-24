1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So the main goal is to find the longest path between two nodes. Only the length as an int is needed
- Since the path can be made from left child, to root, to right child, I need a way to return the length of my current path from the left child and pass it back to the root; and the same for the right. Then the root would return the sum of these two paths
- So it is kind of like a sub problem, at my current node. 
    - I need to get the sum of both the left and right child paths
    - Then what I should return to my parent node is the longest path between the left and right ones
        - I can't return the sum, since the diameter is just one linear path

4. Assess the space/time complexity:
- Space: Since this is a dfs solution, with every node needing to be processed, there will be O(n) recursive calls 
- Time: O(n) for similar reasoning, all n nodes in the BT need to be processed

5. Optional - Give any ways you would improve your solution:
- If I didn't want to use nonlocal, I could have used:
    - self.res = 0 and self.res in the dfs function