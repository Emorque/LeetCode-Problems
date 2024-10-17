1. List out any clarifying questions:
- By splicing, you mean reordering the next values of the already existing nodes right?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Something I could do is create a new head node that is None
- Then, I'll comapre the current nodes in both lists, and whichever is smallest, I set head.next to that node, and then set both head and that smallest list's current nodes to the next node
- I'll keep doing this until both nodes for the lists point to None, all of the nodes have been processed

4. Assess the space/time complexity:
- Space: O(1) since all I have are pointers to nodes in memory, which take up constant space
- Time: O(m+n) since I need to process all nodes in list 1 (n nodes) and in list 2 (m nodes)

5. Optional - Give any ways you would improve your solution: