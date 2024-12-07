1. List out any clarifying questions:
- What should I do with empty digits?

2. List out 1-3 data structures/algorithms that could be useful:
- hashmap
- backtracking

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I need to build some number of phone number combinations, it would be useful to build up to one combination, and then backtrack and build the phone number for the rest of the characters each number represents
- In that way, having a mapping of the numbers to the letters would be useful
- Then, I just start from left to right and use a helper function to perform this backtracking
- The base case will be when I've done all digits for this combination

4. Assess the space/time complexity:
- Space: O(4^n) as in the worse case scnerio of 4 letters for all n numbers, that is 4 recursive calls for each number
- Time: O(4^n) for the same reason

5. Optional - Give any ways you would improve your solution: