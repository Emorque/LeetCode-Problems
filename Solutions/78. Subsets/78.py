from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        collection = []
        subset = []
        def helper(index):
            if index == len(nums):
                collection.append(subset[:])
                return
            subset.append(nums[index])
            helper(index + 1)

            subset.pop()
            helper(index + 1)
        helper(0)
        return collection