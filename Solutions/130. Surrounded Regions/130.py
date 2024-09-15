from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        row = len(board)
        col = len(board[0])

        def bfs(coordinates):
            queue = [coordinates]
            visited = set()

            while queue:
                r, c = queue.pop(0)
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if (r,c) in visited or (r,c) in safe:
                    continue
                visited.add((r,c))

                if board[r][c] == "X":
                    continue
                
                safe.add((r,c))
                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))
        
        for i in range(col):
            if board[0][i] == "O":
                bfs((0, i))
            if board[row - 1][i] == "O":
                bfs((row - 1, i))
        
        for i in range(row):
            if board[i][0] == "O":
                bfs((i, 0))
            if board[i][col - 1] == "O":
                bfs((i, col -1))

        for r in range(row):
            for c in range(col):
                if (r,c) not in safe:
                    board[r][c] = "X"