from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0

        for num in nums:
            output = output ^ num
        
        return output