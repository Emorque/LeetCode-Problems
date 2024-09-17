1. Share questions you would ask to help understand the question:
- Can we ever return 0?
- Are there any negative numbers or 0 in nums?
- What is the expected range for the length of nums?
- What is the expected range for target?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)

3. Write out in plain English what you want to do: 
- By drawing out a decision tree, I realized that the whole time complexity would be 2^n, as we would have to process n nums, and each step, there are two diverging choices. 
  - We can either add or subtract the current number 
- Since this would be too much time complexity, another approach, is to still use a dfs approach, but to include a data structure to store a cache
- How I had the decision tree anyway, was in the form of (index, currentSum)
- So that can be the key, and the value can the number of paths that total that target
- So, as base cases, I would check if the index is at the end
  - If it is, return 1 if the target is equal to the currentSum, meaning that this path leads to the target, so it can be counted towards a totalPath count
    - If not, return 0, this path should not be counted
  - Check if the current (index, currentSum) is in the cache, return the value it is i

- Now comes the recursive part
  - set (index, currentSum) = (dfs(index + 1, currentSum + nums[index]) + dfs(index + 1, currentSum - nums[index]))
    - Basically, from the current index and current Sum, if the first dfs returns 1 and the second returns 1, that means that, when I add the current num, there is path that leads to target, and another path if I substrat the current num
  - return this value

- return dfs(0, 0)

4. Translate each sub-problem into pseudocode:
- explained pretty thoroughly in 3.

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        expressions = {}

        def dfs(index, currentSum):
            if index >= len(nums):
                return 1 if currentSum == target else 0
            if (index, currentSum) in expressions:
                return expressions[(index, currentSum)]
            
            expressions[(index, currentSum)] = dfs(index + 1, currentSum + nums[index]) + dfs(index + 1, currentSum - nums[index])

            return expressions[(index, currentSum)]
        return dfs(0, 0) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this alogrithm is an optimized version of a dfs approach, with the inclusion of a cache making duplicate work not execute
- One weak area, is that as with all dp solutions I have seen so far, you can do from dfs -> dfs with caching -> dp with arrays. I could not figure out how to reach that last step, so I know some optimizations can be made