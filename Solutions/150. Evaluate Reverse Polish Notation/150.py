from typing import List

class Solution:
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
        return stack.pop()