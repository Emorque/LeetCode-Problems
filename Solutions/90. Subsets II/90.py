from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subset = []
        
        def helper(index):
            if index == len(nums):
                subsets.append(subset[:])
                return
            
            subset.append(nums[index])
            helper(index + 1)

            subset.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1)

        helper(0)
        return subsets