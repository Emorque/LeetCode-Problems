from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output, currList = [], []
        candidates.sort()
        startSet = set()
        candLength = len(candidates)

        def dfs(currSum, currIndex):
            subset = set()

            for i in range(currIndex, candLength):
                currCand = candidates[i]
                if currCand in subset:
                    continue
                subset.add(currCand)
                if currSum + currCand == target:
                    currList.append(currCand)
                    output.append(currList.copy())
                    currList.pop()
                elif currSum + currCand < target:
                    currList.append(currCand)
                    dfs(currSum + currCand, i + 1)
                    currList.pop()
                else:
                    break
        for c in range(candLength):
            currCand = candidates[c]
            if currCand == target:
                output.append([target])
                break
            elif currCand > target:
                break
            if currCand in startSet:
                continue
            currList.append(currCand)
            dfs(currCand, c + 1)
            currList.pop()
            startSet.add(currCand)
        
        return output