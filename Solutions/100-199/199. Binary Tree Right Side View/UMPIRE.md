1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Queue

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I am looking to add all the right side nodes, that basically means, for all levels on the BT, return the rightmost node
- In that case, I can perform level order traversal with a queue, the element that is the last to be processed in the level should be the rightmost node for that level
- Using other traversals might be tricky since the rightmost node could be deep in the left subtree

4. Assess the space/time complexity:
- Space: O(m) where m represents the most number of nodes present in a level in the given BT. The size of the queue should not exceed this
- Time: O(n) where n represents all nodes in the BT as they are all processed

5. Optional - Give any ways you would improve your solution: