from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg, mid, end = 0, 0, len(nums) -1

        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                beg += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1