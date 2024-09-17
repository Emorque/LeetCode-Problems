from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        grid = []
        for i in range(len(coins) + 1):
            grid.append([0] * (amount + 1))
            grid[i][0] = 1
        
        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                difference = c - coins[r - 1]
                if difference >= 0:
                    grid[r][c] += grid[r][difference]
                grid[r][c] += grid[r - 1][c]
        
        return grid[-1][-1]