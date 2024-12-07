1. List out any clarifying questions:
- Can I return the sum in reverse order too?
- Can the two given numbers have a different number of digits?

2. List out 1-3 data structures/algorithms that could be useful:
- Two pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I need to return the sum of these two numbers as a new LL, I can kind of treat this like doing long addition, with a carry.
- The thing to note is that the numbers have may a different number of digits, so I'll need to cotinue with the number that has more digits
- I could probably just do something like "if l1", so that a number only gets processed if it has more digits to process

4. Assess the space/time complexity:
- Space: O(1) since I am only using constant extra space
- Time: O(n + m) where n and m represent the number of nodes l1 and l2 have respectively since they all need to be processed

5. Optional - Give any ways you would improve your solution: