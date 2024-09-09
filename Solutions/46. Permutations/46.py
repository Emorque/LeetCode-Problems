from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        output, currList = [], []

        numsLength = len(nums)

        def dfs(currLength):
            if currLength == numsLength:
                output.append(currList.copy())
                return
            for i in range(numsLength):
                if nums[i] not in seen:
                    currList.append(nums[i])
                    seen.add(nums[i])
                    dfs(currLength + 1)

                    currList.pop()
                    seen.remove(nums[i])

        for num in nums:
            seen.add(num)
            currList.append(num)
            dfs(1)
            seen.remove(num)
            currList.pop()

        return output