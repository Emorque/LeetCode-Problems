1. List out any clarifying questions:
- Am I returning a list of strings? Each string is a combination?
- Be well-formed, you mean valid parentheses right?

2. List out 1-3 data structures/algorithms that could be useful:
- Recursion

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So when given the number n, I need to return every combination of n well formed parantheses
- When building a combination, usually I am given two choices, I can either add an opening or closing parentheses. That kind of makes it so that this is a decision tree question
- If that's the case, then the time complexity of building this would grow to 2^n, since I have 2 decisions for n parentheses pairs
- So I need a way to track all my opening parentheses so that I know that I can add a closing validly
- I can't add a closing one if I dont have an opening one before it
- In that case, I can build a function that holds the number of opening and closing parentheses the current combination has. 
- Then, if I have enough to add an opening or a closing, I can make that choice
- But maybe I should do some kind of popping and appending so that is looking like backtracking approach. Once a path is completely, I'll pop and then explore the other path

4. Assess the space/time complexity:
- Space: For this problem, it is a bit complicated, since it boils down to likely an equation to determine, from n, how many possible combinations can be made. Lets say that number if x, then space would be O(x) since each combination needs to be stored and x gets multipled by 2n, since I need to make 2 choices, opening and closing
- Time: The same logic above applies to time: O(x)

5. Optional - Give any ways you would improve your solution: