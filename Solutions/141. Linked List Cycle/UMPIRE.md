1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Two Pointers

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The difference between a LL that has a cycle and one that does not, is that when traversing through the LL, a cycled LL will never return None. It will essentially just keep looping forever
- So, when determining a cycle, if a None is hit when traversing, then I know the LL is not a cycle
- If it is, I can set two pointers are two difference traversal speeds. Evantually, the two will collide, and then I can return True. Without two pointers are differing speeds, the function would never end if given a cycle

4. Assess the space/time complexity:
- Space: O(1) since I am using pointers to track nodes, which are of constant space
- Time: O(n) where n is the number of nodes, since the pointers have to traverse through all n nodes in the LL

5. Optional - Give any ways you would improve your solution: