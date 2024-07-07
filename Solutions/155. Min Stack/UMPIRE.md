1. Share questions you would ask to help understand the question:
- Are we allowed to use more than one data structure?
- Will there be consecutive min stack initializations?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stacks (Likely)
- Queue (Neutral)

3. Write out in plain English what you want to do: 
- So the idea I got is to utilize two stacks, one that acts to mimic the one the user creates, and the other handling the min values
- in push: add the val in the regular stack, and only in the min stack if the val is a new min
- in pop: remove the top values from both stacks 
- in top: get the top value from the regular stack
- in getMin: get the top value from the min stack

4. Translate each sub-problem into pseudocode:
- in init: Initialize two stacks: stack and minStack
- in push: push the val in the regular stack, and only in the min stack if the val is a new min. Else, add the current min value to the top of the min stack again
- in pop: pop from both stacks 
- in top: peek from the regular stack
- in getMin: peek from the min stack
    
5. Translate the pseudocode into Python and share your final answer:
  <!--  
  class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.getMin()) if self.minStack else val  
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]        
   -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it is an easy algorithm to follow through will, and illustrating how test cases work can be easily drawn
- One weak area is that it uses two stacks. There is actually a cool solution that utilizes one stacks and instead of initializing two stacks, you can initialize one stack with: [ (None, float('inf')) ]. Then you just use [0] for the regular stack and [1] for the minStack