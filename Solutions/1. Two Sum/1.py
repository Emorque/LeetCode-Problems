from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in differences:
                return [i, differences[diff]]
            differences[num] = i