class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid = []
        mostOperations = len(word1) + len(word2)
        for i in range(len(word2)):
            grid.append([mostOperations] * (len(word1) + 1))
            grid[i][-1] = len(word2) - i
        
        lastRow = []
        for j in range(len(word1) + 1):
            lastRow.append(len(word1) - j)
        
        grid.append(lastRow)

        for r in range(len(grid) -2 , -1, -1):
            for c in range(len(grid[0]) - 2, -1, -1):
                if word1[c] == word2[r]:
                    grid[r][c] = grid[r + 1][c + 1]
                else:
                    grid[r][c] = min(grid[r + 1][c] + 1, grid[r][c + 1] + 1, grid[r + 1][c + 1] + 1)

        return grid[0][0]