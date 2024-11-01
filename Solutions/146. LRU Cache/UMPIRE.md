1. List out any clarifying questions:
- Does getting a key make it now the most recently used?

2. List out 1-3 data structures/algorithms that could be useful:
- LL
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- That O(1) time complexity really puts a hamper in what I can do
- Off the top of my head, I know popping from a stack is O(1), but the issue comes in making sure the LRU is always the candidate for popping
- When I add a key or update, I need to be able to update this structure and the LRU in O(1)
- Positioning my caches is the priority. Instead of using a list, a similar structure would be to use a LL. The benefit of a LL, is that I can easily remove and append nodes while maintaining the rest of the structure's order in O(1)
- However, I still need to O(1) time complexity, so to remove the need to iterating through the whole LL to find a specific node, I can use a hashmap with the key being the given key and value being the node. Thankfully, hashmaps have O(1) lookup so this'll work still
- To make this work, I'll have a LL structure where the head is my most recently used and my tail is LRU. I'll need a Node class, and also functions to add and remove nodes to make this shuffling easier and be called by both get and put

4. Assess the space/time complexity:
- Space: O(n + n) -> O(n). The ns comes from both the nodes hashmap having n keys and the LL having n nodes, where n is the capacity
- Time: O(1) for all operations

5. Optional - Give any ways you would improve your solution:
- 1000% I would work on readability. There are a lot of self and long references to get a node, I would definetly go back and simplify this to make it more readable if I spent more time