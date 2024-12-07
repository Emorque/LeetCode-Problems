from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        added = set()

        def helper(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return
            
            for num in nums:
                if num in added:
                    continue
                permutation.append(num)
                added.add(num)

                helper(permutation)
                permutation.pop()
                added.remove(num)
            
        helper([])
        return permutations