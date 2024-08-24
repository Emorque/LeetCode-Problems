1. Share questions you would ask to help understand the question:
- Can there be a negative input?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- DP (Likely)

3. Write out in plain English what you want to do: 
- Based on the input, one thing that is guarenteed is that the valid parentheses can only have n opening and closing parentheses
- And, a string can only be valid, if all closing parentheses are after at least one opening parentheses
- A way this can be thought of is like a branching path
- Starting from an empty string, only an opening parentheses string can be added
  - Then a recursive call can be moved, where two difference choices are made:
    - An opening parentheses is added
    - A closing parentheses is added
  - Then from those branches, more branches can diverge
- The base case will append the currently formed string to the output list

4. Translate each sub-problem into pseudocode:
- Initialize an output list 
- Initialize a helper function that takes in the paremeters: open, end, currStr:
  - if the open and end count equal n, then the string is complete:
    - append the currStr to the outputlist
    - return
  - if open <= end: 
    - append '(' to the currStr
    - call helper(open + 1, close, currStr)
  - else: 
    - call helper(open + 1, close, currStr + '(')
    - call helper(open, close + 1, currStr + ')')
- call helper(0, 0, "")
- return the output list

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def helper(open: int, close: int, currStr: str):
            if open == n and close == n:
                output.append(currStr)
                return
            if open == n:
                helper(open, close + 1, currStr+')')
            elif open <= close:
                helper(open + 1, close, currStr+'(')
            else:
                helper(open + 1, close, currStr + '(')
                helper(open, close + 1, currStr + ')')
        helper(0, 0, "")
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, because of the conditionals, every path will evantually lead to a valid string of parentheses. 
- One weak area is that the number of conditionals could have been lesssened by comparing the open count to n instead of close. 