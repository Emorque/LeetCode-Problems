1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Cache with Decision Tree
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This is a decision tree problem with 3 potential decisions at each step, deleting, inserting, or removing
- These choices can be tied down to the current indexes of word1 and word2
- This allows the decision helper function to easily translate into a 2d dp solution

4. Assess the space/time complexity:
- Space: O(m *n)
- Time: O(m *n) where m and n are the lengths of word1 and word2

5. Optional - Give any ways you would improve your solution:
- This of course could be optimized further in terms of space as I would only need to keep 2 rows in memory as that is all the dp solution is looking at