1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- 

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- start with a costs array of size n where each element is infinity
- In the end, return -1 if costs[dst] is equal to infinity, else just return what is there
- Since I want to find the cheapest flight in k stops, I'll have a for loop that iterates k + 1 times
    - Then, I'll create a clone of costs, because I want to set the values in the costs array equal to the min of itself, and costs[from] + price. 
    - If I do this, I'll end up performing multiple flights in one pass, which goes against k stops

4. Assess the space/time complexity:
- Space: O(n) for the 2 arrays
- Time: O(k * len(flights))

5. Optional - Give any ways you would improve your solution: