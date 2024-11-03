1. List out any clarifying questions:
- Is the list sorted in any way?

2. List out 1-3 data structures/algorithms that could be useful:
- Backtracking

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I definetly want to build a subset going from left to right
- Drawing out a decision tree, there are somewhat three choices here
- Starting from nothing, I can add my current number to the subset or not add it
- Then, when deciding on the next path to take, I can either set the index that I am on to be the same, or increase it by 1, essentially moving onto the next number
- What if instead of starting from index 1 and then working up to the end, I called helper with a for loop that has different starting points. Then, I'm am back to only having 2 decisions for each number, keeping the index the same or incrementing it

4. Assess the space/time complexity:
- Space: O(t + n * m) where t represents the depth of the recursion, the number of elements that sum to target, which can vary greatly. n*m comes from the number of combinations that are stored in the result array, n for number of combinations and m for average length  
- Time: O(2^t) as there are two choices for each recursive call and the t is the depth as explained

5. Optional - Give any ways you would improve your solution: