1. Share questions you would ask to help understand the question:
- Both cars are not ordered in any way?
- Are both lists at least length 1?
- Can the target be less than any of the starting positions? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Sorted (Likely)

3. Write out in plain English what you want to do: 
- I think the best way to go about this problem, is to consider the cars that are the closest to the target, and then iterates towards the farther ones
- Then the travel time of these cars in that order can be appended to a stack
- If a car has a greater travel time, then it will intersect with the next car and then become a part of its fleet
  - Since its speed then has to be slower, it doesn't get added to the stack 
- At the end, the length of this stack can be returned as the answer

4. Translate each sub-problem into pseudocode:
- Iterate through the arrays target and position, making them into a pair and appending that to a list
- Sort through that list
- Initialize a stack 
- Iterating from the right to the left, since the cars with the positions closest to the target are to the right
  - If the stack is empty:
    - append the travel time (target - position) / spd 
  - else the stack and the top of the stack's travel time is greater than the current travel time
    - append the current travel time to the stack 
- return the len of the stack 

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road = []
        stack = []
        for i, num in enumerate(position):
            road.append([num, speed[i]])
        
        road = sorted(road)

        for j in range (len(road) - 1, -1, -1):
            tt = (target - road[j][0]) / road[j][1]
            if not stack: 
                stack.append(tt)
            elif stack and stack[-1] < tt:
                stack.append(tt)
        return len(stack) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that if there is a car that will interesect with another car and become a part of it's fleet, it is ignored and not added to the stack
- One weak area is that sorting portion could be done better, with python's built in zip and list comprehension