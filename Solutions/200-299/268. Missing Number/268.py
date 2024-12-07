from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i, num in enumerate(nums):
            missing ^= num
            missing ^= i
        return missing ^ (i + 1)