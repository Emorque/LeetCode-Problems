1. Share questions you would ask to help understand the question:
- Is it guarenteed that the end of nums will always be reached?
- Can a jump be greater than it's distance to the end of the nums list? Bascially, can we overjump at the end?
- Does the end of the nums list always have a number not 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two Pointer (Likely)

3. Write out in plain English what you want to do: 
- After trying to think of a potential solution, I realized that there a lot of test cases that kinda foil some soltutions I came up with
- After some time, I think a two pointer solution (sliding window?) approach can work
  - The saving grace is that the input nums are always guarenteed to reach the end
  - With that being said, from any step, there is essentially a space from it to its value where jumping from it can land you. 
    - So in the case of example 1, at index 0, it can jump to indexs (1, 2)
    - Since this is the first jump, that window of space is where the next window can be found, be seeing which jump from within this window can land the person the farthest. Then, the cycle is repeated until the window reaches the end of the nums list. And every time a new window is created, that will represent a jump

4. Translate each sub-problem into pseudocode:
- initialize a output int and a farthest int to 0
- initialize 2 pointers at 0, since we are starting at index 0 

- while the end pointer < len(nums) - 1:
  - farthest = 0 *start fresh each time
  - for i in range(start, end + 1):
    - farthest = max(farthest, nums[i] + i)
  - start = end + 1
  - end = farthest
  - output += 1
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def jump(self, nums: List[int]) -> int:
        output = 0
        farthest = 0

        start, end = 0, 0

        while end < len(nums) - 1:
            farthest = 0
            for i in range(start, end + 1):
                farthest = max(farthest, nums[i] + i)
            start = end + 1
            end = farthest
            output += 1
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area about this algorithm is that no extra data structures or multiple passes of the nums list are needed, saving space and time
- One weak area is that this problem works only if there is guarenteed to be a way to reach the end. And I should add some context to the for loop. Because, even if the furthest step in the window lands at a 0, that should still be considered the farthest, since there will be another space in the window that will be greater than 0, which can lead to another jump. 