from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target-num] = i
            else:
                return [i, hashmap[num]]
        