1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Binary Search

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This looks to be a great problem for binary search. Since the array is in sorted order, that means I can keep track of three important pointers: left, mid, and right
- I'll set left and right at each end, and then mid between the two. I then check the mid number in relation to the target
  - if mid is > target, than I know that target has to exist between left and mid. I am essentially halfing the array every time, since in this example, there is no need to consider numbers between mid and right
- I'll do this while left <= right, not < since there may be a case where left and right are equal, but they happen to be on the target as well 

4. Assess the space/time complexity:
- Space: O(1) since I am only using three int variables, which each take up O(1) space
- Time: O(logn) since I am essentially halfing the number of elements I need to process each time by half. 

5. Optional - Give any ways you would improve your solution: