1. List out any clarifying questions:
- Can I assume the pops, tops, and getmins will only be called when there is at least one number on the stack?

2. List out 1-3 data structures/algorithms that could be useful:
- Stacks

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I need to emulate a min stack with O(1) time compexities for its functions, using a stack would be very useful. The idea of push, pop, and top should be easy. 
- However, the getMin is a bit tricky
- If I hold the min with an int, I need a way to remember all previous mins. If I pop what was the min, I need to set the int to what was the previous min
- Since there is no way to know how many new mins are set, I theoretically need to hold all values if every value is pushed in decensding order
- So, how about I also use a stack to just hold the min, instead of an int 
- I'll track the min at every push so that I always have a min in memory. Then whenever I pop, I just pop from both stacks 

4. Assess the space/time complexity:
- Space: O(2n) -> O(n) since there will be n calls, and if they are all push calls with each number in decreasing order, then both stacks will have n numbers in them
- Time: O(1) for each function call

5. Optional - Give any ways you would improve your solution: