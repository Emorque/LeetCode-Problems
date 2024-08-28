from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1


        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 
            if low + 1 == high and nums[low] > nums[low + 1]:
                return nums[low + 1]
        return nums[low]