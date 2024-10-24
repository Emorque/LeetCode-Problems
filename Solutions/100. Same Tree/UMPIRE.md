1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- When given nodes p and q, I return True if they represent identical trees
- I think a way to do this could be to first check the node itself, and the recusively call the same function, this time with ps and qs left and right subtrees
- Then, if all three things match, current node, left subtrees, and right subtress, than I can return True for this current node

4. Assess the space/time complexity:
- Space: Since every node needs to be checked, there will be O(n) or O(m) calls, with n being num of nodes in p and m being num of nodes in q. What determines this should be whatever has the fewest number of nodes between the two. In the case where they are the same tree, than O(n) would just be the number of nodes found in each indepdently. 
- Time: Since every node needs to be checked, the time would be O(n + m) for all the nodes in p and q respectively

5. Optional - Give any ways you would improve your solution:

