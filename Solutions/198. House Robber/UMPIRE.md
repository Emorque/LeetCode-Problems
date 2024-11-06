1. List out any clarifying questions:
- Can I assume that there are at least two houses in every test case?

2. List out 1-3 data structures/algorithms that could be useful:
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I'll start from index 2 for each test case
- If the array is length 1 or 2, just return the max 
- Otherwise, the logic in the loop is as follows:
- Set the current index as the max of (itself + index - 2, index-1)
- The logic being at this house, I either rob it and carry the money from the house two houses down, or I skip it and carry over the money I robbed from the previous house
- Return the last index

4. Assess the space/time complexity:
- Space: O(1) since I am using constant space in the bottom solution and only editing the given array in the above solution 
- Time: O(n) since all elements are traversed once

5. Optional - Give any ways you would improve your solution: