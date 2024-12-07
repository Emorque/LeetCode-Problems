1. List out any clarifying questions:
- Are there duplicate numbers?

2. List out 1-3 data structures/algorithms that could be useful:
- Backtracking

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Drawing a decision tree was very helpful, as it shows how for each number, I either add or don't add the current number to my subset
- So for every number, I have two decisions
- To do this in code, I can create a recursive function that carries the current index, and takes on one path that doesn't add the current number and another path that does
- Once the index is at the end, I can add a copy of my created subset to the overall result list

4. Assess the space/time complexity:
- Space: O(2^n) as for each number in the nums list, I make 2 choices, which results in 2 recursive calls on the stack
- Time: O(2^n) for the same reason. This is also illustrated with a decision tree

5. Optional - Give any ways you would improve your solution: