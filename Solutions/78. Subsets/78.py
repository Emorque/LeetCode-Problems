from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, currList = [], []
        numsLength = len(nums)

        def dfs(currIndex):
            if currIndex == numsLength:
                output.append(currList.copy())
                return
            currList.append(nums[currIndex])
            dfs(currIndex + 1)
            currList.pop()
            dfs(currIndex + 1)

        dfs(0)
        return output