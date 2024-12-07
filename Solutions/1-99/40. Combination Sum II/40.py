from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        candidates.sort()

        def helper(index, currentSum):
            if currentSum == target:
                combinations.append(combination[:])
                return
            if currentSum > target or index == len(candidates):
                return
            
            combination.append(candidates[index])
            helper(index + 1, currentSum + candidates[index])

            combination.pop()
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1

            helper(index + 1, currentSum)
        
        helper(0, 0)
        return combinations
            