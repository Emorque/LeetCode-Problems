1. List out any clarifying questions:
- Will I ever divide by 0?
- How should I handle divison?
- Can I assume that the expression is valid one?

2. List out 1-3 data structures/algorithms that could be useful:
- Stack

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- After looking at what reverse polish notation is, it can get a bit tricky if there are expressions within expressions
- The default case does seem to just be (x, y, operation), which translates to (x operation y)
- Since I would have to simplify all inner expressions before being able to solve outer ones, I need a way to track all numbers I have seen thusfar
- Thinking that the inner expressions are just like parentheses in math, what I can do is use a stack
- Because with a stack, I'll keep track of all numbers I've seen
- Then, whenever I come across some operation, I'll pop the two top numbers from my stack since they are the most relevant, and then perform the operation with them. Now that the inner expression is simplified, I'll append the result back to the stack

4. Assess the space/time complexity:
- Space: O(m) since the stack will only contain the number tokens, m represents the number of number tokens in the given list.  
- Time: O(n) where n represents every token in the list, since all of them need to be processed

5. Optional - Give any ways you would improve your solution: