1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The big thing is that I need to construct a deep copy of the given LL, which would be easy if I only have to deal with next, or even next and prev
- The issue lies in that random pointer can point to anywhere, even nodes that are more towards the end of the LL
- So if I am at a node whose random value points to a future node, I need a way to keep that same random value for my deep copy
- It would be useful to have each node in memory, so I think doing that might be a good solution
- I can use a hashmap for easy lookups, where the original node is the key, and the value is a deep copy I make from the first pass
- Then, I can do a second pass where I link up the random and next values 

4. Assess the space/time complexity:
- Space: O(n) as there will be n keys for n nodes
- Time: O(2n) -> O(n) as I need to perform 2 passes of the given LL for this solution

5. Optional - Give any ways you would improve your solution:
- I would like to investigate to see if there are solutions that implement a one pass approach, if possible