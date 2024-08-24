1. Share questions you would ask to help understand the question:
- Could the entire answer array be filled with 0's; each day gets progressively colder?


2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Stack (Likely)
- Queue (Likely)

3. Write out in plain English what you want to do: 
- What this problem has got me thinking, is to use a stack, where, instead of holding the values of the temperatures, it holds the indexes
- Since the temp list is at least 1, the stack can be initalized with index 0
- Then interating throughout the list, if the value at the top of the stack is not less than the current temp, add the current index to the stack
  - if it is, then calculat the differnce between the two indexes and set that to the value to the corresponding index on the output list. And with this approach, I think it could also be done in-place

4. Translate each sub-problem into pseudocode:
- initialize a stack with the index 0: [0]
- set a loop that interates through the temps list from 1 to the end
  - if stack[-1] < current temp:
    - append the current index 
  - else: 
    - set temp[stack[-1]] to the difference between the stack[-1] and the current index
    - pop from the top of the stack 
- return the temp list

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    temp = stack.pop()
                    temperatures[temp] = i - temp 
                stack.append(i)
        while stack:
            temperatures[stack.pop()] = 0
        return temperatures -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution is done in-place, which can save a lot of space if the temperatures array is very large
- One weak area is that I did need to have that final while loop, for the ending temperates that just kept decreasing. I would like to find a way to incorprate different conditionals so that that wouldn't be needed