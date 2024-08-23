1. Share questions you would ask to help understand the question:
- Can there be a case where there is only one nonzero element?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Two pointers (Likely)

3. Write out in plain English what you want to do: 
- What this has got me thinking, is to use use two pointers right away 
- Starting from left to right, have one pointer that is stationary. And then another that keeps going until it reaches a height of p1 or greater
- Then, add the heights of each index minus p1 to an output int

4. Translate each sub-problem into pseudocode:
- initialize a stack and an output int 
- Starting from the left and then incrementing until the end:
  - have a pointer p1 that increments until it reaches a nonzero number
    - once reached, create a pointer p2 that increments so long as it does not encounter a number that is greater or equal to p1 
      - if that number is not reached, append the current height of p2 to a stack
      - else: if p2 reaches a height that is p1 or greater, enter another loop
        - until the stack is empty
          - add the value of p1 - popped value to the output
- return the output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        p1 = 0
        stack = []
        spilled = False

        while p1 != len(height)-1:
            if height[p1] == 0:
                p1 += 1 
                continue
            p2 = p1 + 1
            while height[p2] < height[p1]:
                if p2 == len(height) - 1:
                    stack.append(height[p2])
                    spilled = True
                    break
                stack.append(height[p2])
                p2 += 1
            if spilled: 
                right = stack.pop()
                while stack:
                    temp = stack.pop()
                    if right > temp:
                        output += right - temp
                    else:
                        right = temp
                return output
            while stack:
                output += height[p1] - stack.pop()
            p1 = p2
        return output  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it utitilizes stacks to track all of the elevations that were traveresd, and once processed, they can be skipped
- One weak area is that I did not initialling consider the "spilled" test cases, like [4,2,3], where there was space for water to be trapped
  - While it was addressed, I am not a big fan of the nested while and if statements that addressed it, even if it works