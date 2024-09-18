from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 1:
                nums[i] = nums[i - 1] + 1
            else:
                nums[i] = nums[i //2]
        return nums