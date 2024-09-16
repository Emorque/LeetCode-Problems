from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        numsLength = len(nums)

        if numsLength == 1:
            return nums[0]
        
        if numsLength >= 3: 
            nums[2] += nums[0]
        
        for i in range(3, numsLength):
            nums[i] += max(nums[i - 2], nums[i - 3])
        
        return max(nums[-1], nums[-2])
