1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Stack (Monotonic Stack)

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The brute force approach would be to start at each height and see how far I can extend on both the left and right sides, and then calculate the area. 
- However, another way to think about this problem, is to think how how far each height can go from left to right
- For each height, I need a way to measure the starting index it can be measured at, and a stopping point for which that height can no longer be considerd
- This is where a stack comes in. I can always compare my current height to my previous heights. If I ever come across a height that is less than any of my previous heights, than I know for those previous heights, their stopping point is here and I need to pop them from the stack
    - Before doing so, I also need to calculate the area 

4. Assess the space/time complexity:
- Space: O(n)
- Time: O(n)

5. Optional - Give any ways you would improve your solution: