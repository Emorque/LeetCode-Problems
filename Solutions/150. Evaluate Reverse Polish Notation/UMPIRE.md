1. Share questions you would ask to help understand the question:
- Will there be a case where an operand is not after two expressions or numbers?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Queue (Neutral)

3. Write out in plain English what you want to do: 
- After reading what reverse polish notation is, I've gotten the idea to use a stack. It is the simpliest data strucutre I can think of that fits this problem perfectly.
- As the tokens are iterated, they get appended to the stack, and only when an operator is found, does something unique happen:
    - The two top values get popped and a calculation is performed
- Since the input is always valid and there are no cases of 0 divison, it means less conditionals are needed

4. Translate each sub-problem into pseudocode:
- Initialize a stack
- Iterate through each string in tokens
    - If the current str is an operator:
        - Pop the top two values are save them 
        - Perform the caluclation and push the result back into the stack 
    - Else:
        - push the str to the stack
- return the remaining value left in the stack, that is the answer

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for exp in tokens:
            if exp == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif exp == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif exp == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            elif exp == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            else: 
                stack.append(int(exp))
        return stack.pop() -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area of this algorithm is that it is simple and straight-forward to follow through
- One weak area is that it does use a lot of if statements, one for each operator. There is a creative solution that usings a map to store the operators with the corresponding action, that could be scalable. 