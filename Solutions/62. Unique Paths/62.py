class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            grid.append([1] * n)

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[-1][-1]