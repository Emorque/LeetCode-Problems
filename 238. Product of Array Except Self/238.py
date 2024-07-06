from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        answer = [1] * len(nums)

        for i, num in enumerate(nums):
            answer[i] *= prefix
            prefix *= num

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer