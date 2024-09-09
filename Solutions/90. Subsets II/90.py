from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output, currList = [], []
        numsLength = len(nums)
        nums.sort()

        def dfs(currIndex):
            if currIndex == numsLength:
                output.append(currList.copy())
                return
            currList.append(nums[currIndex])
            dfs(currIndex + 1)

            currList.pop()
 
            if currList and currIndex < numsLength and currList[-1] != nums[currIndex]:
                dfs(currIndex + 1)
            elif not currList:
                dfs(currIndex + 1)

        dfs(0)
        return output