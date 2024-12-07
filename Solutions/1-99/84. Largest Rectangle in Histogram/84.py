from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                maxArea = max(maxArea, h)
            startingPoint = i
            while stack and stack[-1][1] > h:
                index, previousHeight = stack.pop()
                maxArea = max(maxArea, (i - index) * previousHeight)
                startingPoint = index
            stack.append((startingPoint, h))
        
        while stack:
            index, previousHeight = stack.pop()
            maxArea = max(maxArea, (len(heights) - index) * previousHeight)
        
        return maxArea
