from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        queue = deque()
        startColor = image[sr][sc]
        queue.append((sr, sc))

        while queue:
            pixel = queue.popleft()
            row = pixel[0]
            col = pixel[1]
            image[row][col] = color

            if row > 0 and image[row - 1][col] == startColor:
                queue.append((row-1, col))
            if row < len(image) - 1 and image[row + 1][col] == startColor:
                queue.append((row+1, col))

            if col > 0 and image[row][col - 1] == startColor:
                queue.append((row, col - 1))
            if col < len(image[0]) - 1 and image[row][col + 1] == startColor:
                queue.append((row, col + 1))
        return image