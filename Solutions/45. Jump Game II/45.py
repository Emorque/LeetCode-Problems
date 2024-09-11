from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        output = 0
        farthest = 0

        start, end = 0, 0

        while end < len(nums) - 1:
            farthest = 0
            for i in range(start, end + 1):
                farthest = max(farthest, nums[i] + i)
            start = end + 1
            end = farthest
            output += 1
        return output