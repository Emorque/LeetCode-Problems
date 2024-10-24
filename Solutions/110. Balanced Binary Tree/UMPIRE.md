1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DFS

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So, for every node, I want to check if the depth of the left and right subtrees differ no more than 1. If they do, I need to return False. If all nodes are height balanced, I return True
- So, I can use DFS for traversal and when I am at a node, I'll compare the left and right subtrees
    - if they have a difference of at most 1, then alls good
    - else, I can then return -1
- Then, if I ever come across a child that has a height of -1, I know that I no longer need to keep iterating as the BT is already determined to not be height-balanced

4. Assess the space/time complexity:
- Space: O(n) as the worst case scenerio for trees that are not balanced at all and have each node on its own level, meaning that there will be n recursive calls. O(logn) would be best, if the tree was balanced, as it would half the number of calls made. (all nodes have two children if possible)
- Time: O(n) since all nodes would need to be processed to ensure that 

5. Optional - Give any ways you would improve your solution: