from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        number = 0
        left, right= 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            number += 1
            left = right
            right = farthest
        return number
            