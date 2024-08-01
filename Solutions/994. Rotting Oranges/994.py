from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minute = -1
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0: return 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row > 0 and row < len(grid)) and grid[row-1][col] == 1:
                    q.append((row - 1, col))
                    grid[row-1][col] = 2
                    fresh -= 1
                if (row > -1 and row < len(grid) - 1) and grid[row+1][col] == 1:
                    q.append((row + 1, col))
                    grid[row+1][col] = 2
                    fresh -= 1
                if (col > -1 and col < len(grid[0]) - 1) and grid[row][col+1] == 1:
                    q.append((row, col+1))
                    grid[row][col+1] = 2
                    fresh -= 1
                if (col > 0 and col < len(grid[0])) and grid[row][col-1] == 1:
                    q.append((row, col-1))
                    grid[row][col-1] = 2
                    fresh -= 1

            minute += 1  
            
        return -1 if fresh != 0 else minute