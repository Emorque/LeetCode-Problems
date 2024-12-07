1. List out any clarifying questions:
- Can I assume the word will have at least one letter

2. List out 1-3 data structures/algorithms that could be useful:
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I'll iterate through the board until I find a cell that has the first letter in my word
- Then I can enter a helper function that checks the neighboring cells to see if a path can be found
- I will need to use a set to house all my current used cells, as I cannot reuse cells in my path

4. Assess the space/time complexity:
- Space: O(n*m) in the case where I would have to explore each cell recursively
- Time: O(n*m) for that same reasoning

5. Optional - Give any ways you would improve your solution:
- While my solution is average, there are many more optimized solutions that are very interested and seem to utilize a hashmap for frequencies. I'll revisit these solutions on why/how they work