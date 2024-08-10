from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output: List[List[int]] = []
        currVisited = set()
        pacific, atlantic = False, False
        rows =  len(heights)-1
        columns = len(heights[0])-1

        def dfs(currCell: List[int], startCell: List[int]):
            nonlocal pacific
            nonlocal atlantic
            i = currCell[0]
            j = currCell[1]
            if (i,j) in currVisited or (pacific and atlantic):
                return
            if currCell[0] == 0 or currCell[1] == 0:
                pacific = True
            if currCell[0] == rows or currCell[1] == columns:
                atlantic = True
            if pacific and atlantic:
                output.append(startCell)
                return
            currVisited.add((i,j))
            if i > 0 and heights[i][j] >= heights[i - 1][j]:
                dfs([i-1, j], startCell)
            if i < rows and (heights[i][j] >= heights[i + 1][j]):
                dfs([i+1, j], startCell)

            if j > 0 and heights[i][j] >= heights[i][j-1]:
                dfs([i, j-1], startCell)
            if j < columns and heights[i][j] >= heights[i][j+1]:
                dfs([i, j+1], startCell)
        for i in range(rows+1):
            for j in range(columns+1):
                dfs([i,j], [i,j])
                pacific, atlantic = False, False
                currVisited = set()
        return output