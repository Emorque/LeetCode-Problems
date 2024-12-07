1. List out any clarifying questions:
- Can the cost list be a length less than 2?

2. List out 1-3 data structures/algorithms that could be useful:
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The imporant thing is that I need to know the min cost of reaching to the top. 
- A way to break this up into a smaller problem, is to then calcualte what the min cost is to reach each step.
- Since I can climb either 1 or 2 steps, the min cost of each step should be the cost of itself and the min of the 2 previous steps. I would only want to take the min as in the end, I need to work my way up the staircase to reach the top and return the min cost
- Starting from index 2, I'll do just this logic, then at the end, return the min cost of the last 2 steps, since I can reach the top from cost[-2] and cost[-1]

4. Assess the space/time complexity:
- Space: O(1) since I even thought I am not creating anything extra, something like min will use temp variables to compute
- Time: O(n) as I need to process every step in the given cost list of n steps

5. Optional - Give any ways you would improve your solution: