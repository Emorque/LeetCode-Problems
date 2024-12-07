from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        def helper(index, currentSum):
            if currentSum == target:
                combinations.append(combination[:])
                return
            if currentSum > target or index == len(candidates):
                return
            
            combination.append(candidates[index])
            helper(index, currentSum + candidates[index])

            combination.pop()
            helper(index + 1, currentSum)

        for i in range(len(candidates)):
            num = candidates[i]
            if num > target:
                continue
            combination.append(num)
            helper(i, num)
            combination.pop()
            
        return combinations