1. Share questions you would ask to help understand the question:
- Can any costs be negative or 0?
- Are we guarenteed at least two steps?
- Can the last step we take be the last two numbers in the list?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- After going through an example logic, I realized that to reach a step, the ideal choice to get go from the step that costs the least (from the choice of two prev steps):
    - [1,2,3]
    - If I want to reach 3 in the least cost and my options are index 0, and 1. I would want to go with the step that costs the least (index 0)
- since we start from either index 0 or 1, we can iterate from index 2 to the end and just perform this logic. 
- the last index should be the path of the lowest cost

4. Translate each sub-problem into pseudocode:
- for i in range(2, len(cost)):
    - cost[i] += min(cost[i - 1], cost[i - 2])
- return cost[-1]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2]) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm does work inplace and builds on top of previous work