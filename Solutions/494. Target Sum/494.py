from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        expressions = {}

        def dfs(index, currentSum):
            if index >= len(nums):
                return 1 if currentSum == target else 0
            if (index, currentSum) in expressions:
                return expressions[(index, currentSum)]
            
            expressions[(index, currentSum)] = dfs(index + 1, currentSum + nums[index]) + dfs(index + 1, currentSum - nums[index])

            return expressions[(index, currentSum)]
        return dfs(0, 0)