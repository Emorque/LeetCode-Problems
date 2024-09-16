from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] #Can be removed if last line is max(nums[0], bounty, b2)

        b1, b2 = 0, 0

        for i in range(len(nums) - 1):
            temp = max(nums[i] + b1, b2)
            b1 = b2
            b2 = temp

        bounty = b2

        b1, b2 = 0, 0

        for i in range(1, len(nums)):
            temp = max(nums[i] + b1, b2)
            b1 = b2
            b2 = temp

        return max(bounty, b2)