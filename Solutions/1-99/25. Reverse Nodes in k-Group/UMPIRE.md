1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Lists
- Two Pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The easiest way to go about this problem, is to create an actual list from the LL and reverse with either the built in reverse method or via two pointers. Then, convert these lists to LLs, and merge them 
- The most complex solution, which works in O(1) space, would be to just use pointers. 
  - Set up two pointer to act as the boundary (just this space will be reversed), and then just treat this section of the LL as if I am performing a reverse LL solution. 

4. Assess the space/time complexity:
- Space: O(1)
- Time: O(n) since each node is only processed twice(traversing and then the reversal) 

5. Optional - Give any ways you would improve your solution: