1. Share questions you would ask to help understand the question:
- If the whole string s is just *, do I return True

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)

3. Write out in plain English what you want to do: 
- After coming up with a few test cases I think I found a number of rules that can be used in an alogrithm:
  - I can try to have a starCount variable, since when we come across a star, at that point it is hard to tell if it be can used as a paratheses or an empty string, so it just gets held onto
  - Use a stack for the parenthese, if we come across a right parenthese and the top of the stack has a left, pop both
  - If we come across a right p, and star count is greater than the length of the stack, continue as the star can be a left for the right 
  - else return False

4. Translate each sub-problem into pseudocode:
- Set a starCount int to 0
- Initialize a stack

- for char in s:
  - if char is '*':
    - starCount += 1
  - if char is '('
    - append to stack
  - elif char is ')' and starCount > len(stack):
    - count -= 1
    - continue
  - elif char is ')' and stack and stack[-1] == '('
    - stack.pop()
    - continue
  - else:
    - return False
- return True

- Another approach is to use two numbers, one to track the choice of using the star as a (, and one for if we choose to treat it as a )
- Because of this diverging path, my solution of using the stack and one variable had trouble knowing both possible paths

- initalize two int variables, leftMin, leftMax (min number of '(', max number of ')')
- iterate through the string
  - if '*':
    - leftMin -= 1
    - leftMax += 1
  - if '(':
    - leftMin += 1
    - leftMax += 1
  - if ')':
    - leftMin -= 1
    - leftMax -= 1
  - if leftMax < 0:
    - return False # there are more right parentheses than are stars/( that can even it out
  - if leftMin < 0: # the string can still be valid since leftMax is greater than 0, so reset leftMin to 0
    - leftMin = 0 # ex: ( * ) (
- return leftMin == 0

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for char in s:
            if char == '*':
                leftMin -= 1
                leftMax += 1
            elif char == '(':
                leftMin += 1
                leftMax += 1
            else:
                leftMin -= 1
                leftMax -= 1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        return leftMin == 0  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algrorithm is done linearly, and done with no extra data structures, just two ints holding the range of left parantheses
- One weak area is that this is not the most intuitive solution, so understanding the reasoning of the code from just this is not the most clear