1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Binary Search

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Given the logn time constraint, binary search seems like the way to go
- However, given that the nums array is rotated 1-n times, it is not as simple as traditional binary search
- I need to edit my conditions

4. Assess the space/time complexity:
- Space: O(1) because I am using constant extra space
- Time: O(logn) because I'm halving my work with binary search

5. Optional - Give any ways you would improve your solution:
- I do see other logic for the inner conditionals. I'll look into the reasoning and why they work as well 