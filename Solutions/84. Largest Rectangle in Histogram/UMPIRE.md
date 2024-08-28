1. Share questions you would ask to help understand the question:
- Can the rectanles be horizontal?
- Can a bar have no or negative height?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Two pointer (Unlikely)

3. Write out in plain English what you want to do: 
- On paper, if I were to do the problem myself, I would look at each bar in and see the distance it can go to the right. 
- For example: [2, 1, 5, 6, 2, 3]
  - index 0 can't go the right, so its max area is 2
  - index 1 can go to the right till the end and left one since it's less than the prev bar: 5
  - index 2 can go to the right twice: 10
  - index 3 can't go to the right: 6
  - ...
- Using this logic, since bars do need to be compared to the previous bar for cases like index 1, a stack can be used
- In this case, a stack containing the left-most index and height of the bar can help with calculations

4. Translate each sub-problem into pseudocode:
- Initialize a stack 
- Initialize a maxArea int 

- Iterating through the heights array:
  - left is set to the current index 
  - Enter a while loop if the top of the stack has a height greater than the current height
    - pop from the stack
    - calculate the area of that rectangle: popped height * (current index - the popped index) 
    - Use max to get the maxArea
    - left is equal to popped index now 
  - append to the stack that pair (left, current height)

- There may be leftover heights if they can extend all the way to the end
  - Popping from the top, calculate the area: popped height * (len(heights) - popped index)
  - Calculate the maxArea
- Return the maxArea

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []

        for i, h in enumerate(heights):
            left = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                currArea = height * (i - index)
                maxArea = max(maxArea, currArea)
                left = index
            stack.append((left, h))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is done from one traversal of the heights array 
- One weak area is that it could be made more clear what the stack is meant to represent