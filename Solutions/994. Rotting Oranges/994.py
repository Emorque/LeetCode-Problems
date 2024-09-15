from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, timer = 0, 0
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return timer
        
        while queue:
            for k in range(len(queue)):
                r, c = queue.pop(0)
                if r > 0 and grid[r - 1][c] == 1:
                    queue.append((r - 1, c))
                    grid[r-1][c] = 2
                    fresh -= 1
                if r < len(grid) - 1 and grid[r + 1][c] == 1:
                    queue.append((r + 1, c))
                    grid[r+1][c] = 2
                    fresh -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    queue.append((r, c - 1))
                    grid[r][c-1] = 2
                    fresh -= 1
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2
                    fresh -= 1
            timer += 1
        
        return timer - 1 if fresh == 0 else -1