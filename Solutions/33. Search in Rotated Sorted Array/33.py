from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else: 
                    high = mid - 1
            else: 
                if target > nums[high] or target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1