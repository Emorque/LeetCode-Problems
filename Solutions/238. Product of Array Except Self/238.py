from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            products[i] *= product
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= product
            product *= nums[i]
        return products