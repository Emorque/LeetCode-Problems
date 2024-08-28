from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []

        for i, h in enumerate(heights):
            left = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                currArea = height * (i - index)
                maxArea = max(maxArea, currArea)
                left = index
            stack.append((left, h))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea