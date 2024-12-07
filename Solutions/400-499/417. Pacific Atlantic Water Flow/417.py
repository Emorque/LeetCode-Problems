from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(coordiantes, ocean):
            queue = [coordiantes]

            while queue:
                r, c = queue.pop(0)

                if (r,c) in ocean:
                    continue
                ocean.add((r,c))

                if r > 0 and heights[r - 1][c] >= heights[r][c]:
                    queue.append((r- 1, c))
                if r < row - 1 and heights[r + 1][c] >= heights[r][c]:
                    queue.append((r + 1, c))

                if c > 0 and heights[r][c -1] >= heights[r][c]:
                    queue.append((r, c -1))
                if c < col - 1 and heights[r][c + 1] >= heights[r][c]:
                    queue.append((r, c + 1))

        for i in range(col):
            bfs((0, i), pacific)
            bfs((row - 1, i), atlantic)
        
        for j in range(row):
            bfs((j, 0), pacific)
            bfs((j, col - 1), atlantic)
        
        result = []
        for cell in pacific:
            if cell in atlantic:
                result.append(cell)
        return result