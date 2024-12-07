from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # obtain the left and right max heights at each index
        leftMaxes = [0] * len(height)
        rightMaxes = [0] * len(height)

        for i in range(1, len(height)):
            leftMaxes[i] = max(leftMaxes[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            rightMaxes[i] = max(rightMaxes[i + 1], height[i + 1])

        # calculate the max water containable in a vaccum at each index
        total = 0
        for i, h in enumerate(height):
            constraint = min(leftMaxes[i], rightMaxes[i])
            if constraint == 0:
                continue
            water = constraint - h
            if water >= 0:
                total += water 

        # return the cummulative sum 
        return total