1. Share questions you would ask to help understand the question:
- Can we overshoot a step?
- What are the minimum number of stairs?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- What I am thinking is using two integers, that represent taking one or two steps. As a base case, they can both be set to one
- Then n times:
  - we want to take the sum of both numbers, set it to one, and then set what was one previously to two

4. Translate each sub-problem into pseudocode:
- one, two = 1, 1
- for i in range(n - 1)
  - temp = one
  - one = one += two
  - two = temp

- return one

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm does only use ints for space and is done in linear time.
  - I had previous solutions in my head or doing a recursive call, and then simplied to an array of size n, to then simplifying to this solution
- One weak area is that since this solution has been simplified as much as possible, I should have added a comment explaining why summing these two ints leads to an answer