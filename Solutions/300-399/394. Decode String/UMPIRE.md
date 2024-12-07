1. Share questions you would ask to help understand the question:
- Could an integer be 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Recursion (Likely)

3. Write out in plain English what you want to do:
- This problem reminds me of the valid parenthesis problem, where a stack was used and the conditionals depended on whether the current char was opening or closing
- So, a similar logic could be used for this. 
- Start with an empty stack
- Then, are I iterate through the str, create a new string that represents the string within the brackets
- Then, do the same, but for the digits
- Use these two strings to create the whole string, and add that back to the stack, since these k[] can be nested 
- Once the stack is only letters, return it as a string

4. Translate each sub-problem into pseudocode:
- Starting with an empty stack
- Then, iterate through the str 
    - if the char is not ']'
        - append that char to the stack 
    - else:
        - create a new string: temp which will represent the string in the brackets
        - while the top of the stack is not '[':
            - append stack.pop to the temp string, maintaining the correct ordering
        - pop once more for the '[' char

        - now, do it again, for the digits
        - create a num string
        - while the stack has content and the top of the stack is a digit:
            - append stack.pop to the num string, maintaining order
        - use multiplcation, to append temp * num to the stack 
- return: "".join(stack), at this point, it should all be letters

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(temp * int(num))
        return "".join(stack) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area, is that this solution is done without the recursion stack
- One weak area is that this solution does require that newly created substrings are added back into the stack. So a large string from something like "50[absd]" would be added back to the stack. This then further exasterbates if this were in a nested k[].
- One weak area, is that I did have to see NeetCode's video. But, once I saw temp = stack.pop() + temp, it immediately clicked in my mind. I knew that a stack could be used, but it completely flew over my head how I could appreciate popping from the stack while maintaining the ordering
