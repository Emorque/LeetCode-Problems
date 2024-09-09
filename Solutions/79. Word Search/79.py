from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowSize = len(board)
        colSize = len(board[0])

        coordinates = set()

        def dfs(currCell, currIndex):
            row, col = currCell[0], currCell[1]

            if currCell in coordinates or row >= rowSize or row < 0 or col >= colSize or col < 0 or board[row][col] != word[currIndex]:
                return False
            if currIndex == len(word) - 1:
                return True

            coordinates.add(currCell)

            found = dfs((row - 1, col), currIndex + 1) or dfs((row + 1, col), currIndex + 1) or dfs((row, col - 1), currIndex + 1) or dfs((row, col + 1), currIndex + 1)

            coordinates.remove(currCell)

            return found

        for i in range(rowSize):
            for j in range(colSize):
                if board[i][j] == word[0]:
                    if dfs((i,j), 0):
                        return True
        return False