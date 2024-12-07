from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > currSum and currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum 