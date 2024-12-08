1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Preorder

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- My first thought was to figure out what traversals work
- Preorder and inorder worked together, as they helped me figure out the roots and left/right subtrees respectively. 
- I would then iterate through the tree twice, create these two traversals are strings, and then connect them with a seperator like "#"
- However, looking at just preorder again, it may be all I need. The only thing is that, if I add the None children in my string, then I could know when the subtrees start.
- Once I come across a "null", that means that I can just return None in deserialization, and then look to the next value in my string. I can do this will some external index var

4. Assess the space/time complexity:
- Space: O(n) for both functions as all n nodes need to be explored
- Time: O(n) for the same reason

5. Optional - Give any ways you would improve your solution: