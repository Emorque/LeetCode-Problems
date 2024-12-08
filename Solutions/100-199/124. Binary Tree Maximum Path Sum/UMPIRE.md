1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Postorder Traversal

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Drawing an example with some negative numbers sprinkled in there helped me visualize a solution. 
- Since I need to determine the highest pathsum at each node, I would have to know what paths the node's children each have. 
    - In that case, I needed to use post order traversal (recursively call both children first, then process current node)
- And if a node doesn't exist, just return 0, thats a good base case as it won't add/subtract from a path
- Now, both child nodes should be processed. When thinking of the current best path, I'll have a currentSum int var
    - This var will be set to the current node's value at the start. 
    - I should only add the child nodes if they have positive sums. This is because there is no need to add negative subtress to my path. If my right subtree is negative, I can just disregard it, same for left
- Then, just set a maxNum var to max(maxNum, currentSum)
- Finally, I need to return something which may not be currentSum. CurrentSum could connect both the current node to the left and right subtrees. 
- However, when returning to the parent node, I can't return this path. The only valid path I can return is current node, curr + left or curr + right. So, I'll just return the max of these paths
- In the end, return maxNum

4. Assess the space/time complexity:
- Space: O(n) for all nodes as they all need to be checked (recursive stack)
- Time: O(n) for the same reason

5. Optional - Give any ways you would improve your solution: