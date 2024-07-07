from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_sequence : int = 1
        curr_sequence : int = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] : continue
            if nums[i] + 1 == nums[i+1]:
                curr_sequence += 1
            else:
                longest_sequence = max(longest_sequence, curr_sequence)
                curr_sequence = 1
        return max(curr_sequence, longest_sequence)
