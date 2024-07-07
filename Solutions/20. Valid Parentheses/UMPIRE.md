1. Share 2 questions you would ask to help understand the question:
  -  What should returned if the string is empty or null?
  -  What should be do if there is a character in the string that is not a bracket?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
  - Stack: Likely
  - Set: Unlikely
  - Linked List: Unlikely
  
3. Write out in plain English what you want to do: 
  - First, we want to create stack because we can utilize 'pop' to close any 'open' brackets
  - Then as we iterate through the string, we add the current character to the stack if the stack is empty, or the character is an 'open' bracket
  - If the character is a 'close' bracket, one of two things will happen:
    1. We can use peek and if the top element in the stack corresponds to the current character, we use pop to remove that top element and continue iterating
    2. If the top element does not correspond, the string is invalid, are we return false
  - Once we iterated through the whole list, one of two things will happen:
    1. If the stack is empty, we return true
    2. Else, we return false as we still have leftover 'open' brackets

4. Translate each sub-problem into pseudocode:
  - initiate the stack and add the first character to it
  - iterate through s:
    - if the character is an opening bracket, append to stack
    - else if the length of the stack is equal to 0, return false
    - else if the character is a closing bracket and matches the top of the stack, pop the stack
    - else, return false
  - return if the stack is empty 
    
5. Translate the pseudocode into Python and share your final answer:
  <!--   stack = []
  stack.append(s[0])

  for i in range(1, len(s)):
    print(s[i])
    if (s[i] == ('(') or s[i] == ('[') or s[i] == ('{')):
      stack.append(s[i])
    elif (len(stack) == 0):
      return False
    elif (s[i] == (')') and stack[-1] == ('(')):
      stack.pop()
    elif (s[i] == (']') and stack[-1] == ('[')):
      stack.pop()
    elif (s[i] == ('}') and stack[-1] == ('{')):
      stack.pop()
    else:
      return False
  return (len(stack) == 0) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
  - Strength: there are no nested if statements, allowing for a single set of if conditionals
  - Weakness: because of that, it is not as readable as it would have been and could have been executed better had I used a map of {opening bracket: closing bracket}