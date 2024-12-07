1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Stack

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- A way that helped me visualize this, was as a spiral, where I slowly go towards the middle, as I go from L0, to Ln, to L1, to Ln-1... 
- That also means that the middle node will always end up at the tail node in the result LL
- I can use slow,fast pointers to get the middle
- Since this is not a DLL, I need a way to track inorder my nodes from middle to tail
- A way I can have a record of these nodes is to use a stack and store the nodes there

4. Assess the space/time complexity:
- Space: O(n/2) -> O(n) as only half of the nodes are in the stack at most. In the end, the stack has 0 elements in it
- Time: O(n) as all the nodes are traversed, with 3 passes

5. Optional - Give any ways you would improve your solution: