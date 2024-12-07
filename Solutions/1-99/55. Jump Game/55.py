from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 1

        for num in nums:
            jump -= 1
            if jump < 0:
                return False
            if num > jump:
                jump = num
        return jump >= 0