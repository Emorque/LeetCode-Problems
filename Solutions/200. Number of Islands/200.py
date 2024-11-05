from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            while queue:
                r, c = queue.popleft()
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if grid[r][c] != "1":
                    continue
                grid[r][c] = "0"
                queue.append((r-1,c))
                queue.append((r+1,c))
                queue.append((r,c-1))
                queue.append((r,c+ 1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count