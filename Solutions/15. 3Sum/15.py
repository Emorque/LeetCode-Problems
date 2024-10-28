from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0
        while i < len(nums) - 2:
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            while left < right:
                pair = nums[left] + nums[right]
                if pair == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif pair < target:
                    left += 1
                else:
                    right -= 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return triplets