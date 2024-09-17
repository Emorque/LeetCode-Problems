class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = []
        for i in range(len(text2) + 1):
            grid.append([0] * (len(text1) + 1))
        
        for r in range(1, len(text2) + 1):
            for c in range(1, len(text1) + 1):
                if text2[r - 1] == text1[c - 1]:
                    grid[r][c] = 1 + grid[r - 1][c - 1]
                else:
                    grid[r][c] = max(grid[r-1][c], grid[r][c-1])
        
        return grid[len(text2)][len(text1)]