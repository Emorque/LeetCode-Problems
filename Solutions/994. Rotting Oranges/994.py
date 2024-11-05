from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        timer = 0
        fresh = 0
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue:
            timer += 1
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r > 0 and grid[r-1][c] == 1:
                    fresh -= 1
                    grid[r-1][c] = 2
                    queue.append((r-1, c))
                if r < row - 1 and grid[r+1][c] == 1:
                    fresh -= 1
                    grid[r+1][c] = 2
                    queue.append((r+1, c))
                if c > 0 and grid[r][c-1] == 1:
                    fresh -= 1
                    grid[r-1][c] = 2
                    queue.append((r, c-1))
                if c < col - 1 and grid[r][c+1] == 1:
                    fresh -= 1
                    grid[r][c+1] = 2
                    queue.append((r, c+1))
        return timer - 1 if fresh == 0 else -1 