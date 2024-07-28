from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        output = 0
        curr = 0

        def traverse(i: int, j: int):
            grid[i][j] = 0
            nonlocal curr
            curr += 1
            if i + 1 < row and grid[i + 1][j] == 1:
                traverse(i + 1, j)
            if i - 1 > -1 and grid[i - 1][j] == 1:
                traverse(i - 1, j)
            if j + 1 < column and grid[i][j + 1] == 1:
                traverse(i, j + 1)
            if j - 1 > -1 and grid[i][j - 1] == 1:
                traverse(i, j - 1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    curr = 0
                    traverse(i, j)
                    output = max(output, curr)

        return output