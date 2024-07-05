1. Share questions you would ask to help understand the question:

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stacks (Likely)
  
3. Write out in plain English what you want to do: 
- We are given the requirement to implement a FIFO queue with 2 stacks
- Therefore, we can set one stack to be the one that takes in new values, and another to handle popping and peeking
- When we add values, we append to stack1
- When we need to pop or peek, if stack 2 is non empty, we pop/peek from there
    - if stack 2 is empty, we just pop all the values from stack1, append them to stack 2, and then pop/peek from stack 2

4. Translate each sub-problem into pseudocode:
__init__:
- initialize two stacks: pushStack, popStack

push
- append x to the pushStack

pop
- if popStack is empty:        
    - while pushStack is non empty, pop all values from pushStack and append to popStack
    - return the value from popping the popStack
- else if popStack is nonEmpty
    - return the value from popping the popStack

peek
- if popStack is empty:        
    - while pushStack is non empty, pop all values from pushStack and append to popStack
    - return the value from the top of the popStack
- else if popStack is nonEmpty
    - return the value from the top of the popStack       

empty
- return (popStack.isEmpty and pushStack.isEmpty)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class MyQueue:

    def __init__(self):
        self.popStack = []
        self.pushStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            return self.popStack.pop()
        else:
            return self.popStack.pop()

    def peek(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            return self.popStack[-1]
        else:
            return self.popStack[-1]

    def empty(self) -> bool:
        return (not self.popStack) and (not self.pushStack) -->



6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it utilizes stack logic to always have the front and back of queue available
- One weak area is that it contains inner functions. With some restructoring, that could be removed