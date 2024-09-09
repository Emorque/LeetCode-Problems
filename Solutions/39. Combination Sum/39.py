from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, currList = [], []
        candLength = len(candidates)

        def dfs(currSum, currIndex):
            for i in range(currIndex, candLength):
                currNum = candidates[i]

                if currSum + currNum == target:
                    currList.append(currNum)
                    output.append(currList.copy())
                    currList.pop()
                elif currSum + currNum < target:
                    currList.append(currNum)
                    dfs(currSum + currNum, i)
                    currList.pop()
        
        for c in range(candLength):
            if candidates[c] == target:
                output.append([target])
            elif candidates[c] < target:
                currList.append(candidates[c])
                dfs(candidates[c], c)
                currList.pop()

        return output