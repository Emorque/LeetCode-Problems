from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        maxArea = 0

        def bfs(r,c) -> int:
            print(r,c)
            area = 0

            queue = deque()
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if grid[r][c] != 1:
                    continue
                grid[r][c] = 0
                area += 1

                queue.append((r+1, c))
                queue.append((r-1, c))
                queue.append((r, c+1))
                queue.append((r, c-1))
                
            return area
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        
        return maxArea