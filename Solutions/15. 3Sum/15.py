from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        visited = set()

        for i in range(len(nums) - 2): 
            if nums[i] in visited:
                continue
            target = nums[i] * -1
            hashmap = {}
            for j in range(i + 1, len(nums)):
                if nums[j] not in hashmap:
                    hashmap[target-nums[j]] = nums[j]
                else:
                    curr = (nums[i], hashmap[nums[j]], nums[j])
                    curr = tuple(sorted(curr))
                    triplets.add(curr)
            visited.add(nums[i])
        return triplets