1. List out any clarifying questions:
- Can there be a case where I am given an empty array or array of length 1?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I would need to keep track of some maxProfit. 
- And every time I process a day, I need to consider some possibilities
    - Can I sell on this day and yeild a greater profit that what I currently have as my maxProfit
    - Should this be the day that I buy to then sell in the future?
- All in all, I think keeping track of some minPrice and maxProfit can help keep track of both things

4. Assess the space/time complexity:
- Space: O(1), since I am only using three extra int variables, which are each O(1) space
- Time: O(n), since I need to process all prices in the given list. So if there are n prices in the list, I need to process all n of then

5. Optional - Give any ways you would improve your solution: