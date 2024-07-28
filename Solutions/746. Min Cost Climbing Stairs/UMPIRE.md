1. Share questions you would ask to help understand the question:
- Can there by less than 2 steps?
- Can there be cases where there are two journeys that have the same costs?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Dynamic Programming (Likely)
- Bottom-Up (Likely)

3. Write out in plain English what you want to do: 
- So, from this problem, you can only go up at 1 or 2 steps at a time.
- This means that the steps from the 2 second step onward is just a sum of the current step's cost + the less of the steps' costs that are right below it (step right below it and the step below that one)
- So, what can be done, is that I iterate through the given input at index 2 and then iterate, changing the current step to the sum of its costs to the min of the 2 previous steps
- Then, return the min of the top of steps, since you can go from the 2 to the last step to the end

4. Translate each sub-problem into pseudocode:
- initialize costLength by calculating length of cost
- for i in range (2, costLength -1):
    - cost[i] = cost[i] + min(cost[i-1], cost[i-2])
- return min(cost[costLength]-1, cost[costLength]-2)

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costLength = len(cost)
        for i in range(2, costLength):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return min(cost[costLength - 1], cost[costLength -2]) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that my algorithm does not use additional data structures nor a recursion stack, it just edits the given input
- One weak area is that it may not be the most readible algorithm