1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Queue

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Because we are just looking to return the BT in level order, a queue would be a great way to do the traversal as appending nodes by level can be done natively 
- I do need to check if root exists before appending it to the queue, as just appending it at all times will still process None as an element in the while loop

4. Assess the space/time complexity:
- Space: O(m) where m represents the most number of nodes present in a level on the given BT. The size should not exceed this number
- Time: O(n) where n represents the number of nodes in the BT

5. Optional - Give any ways you would improve your solution: