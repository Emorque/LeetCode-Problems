from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        marked = set()

        def bfs(coordinates) -> bool:
            pacific, atlantic = False, False
            visited = set()
            queue = [coordinates]
            
            while queue:
                r, c = queue.pop(0)
                if r == 0 or c == 0:
                    pacific = True
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlantic = True
                if pacific and atlantic or (r,c) in marked:
                    return True
                if (r, c) in visited:
                    continue

                visited.add((r,c))

                if r > 0 and heights[r - 1][c] <= heights[r][c]:
                    queue.append((r - 1, c))
                if r < len(heights) - 1 and heights[r + 1][c] <= heights[r][c]:
                    queue.append((r + 1, c))

                if c > 0 and heights[r][c - 1] <= heights[r][c]:
                    queue.append((r, c - 1))
                if c < len(heights[0]) - 1 and heights[r][c+1] <= heights[r][c]:
                    queue.append((r, c + 1))
            return pacific and atlantic 
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs((i, j)):
                    output.append([i, j])
                    marked.add((i,j))
        
        return output
        

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        output = []

        row = len(heights)
        col = len(heights[0])

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

        for height in pacific:
            if height in atlantic:
                output.append(height)

        return output
        