from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        safe = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()
                if r < 0 or r > row - 1 or c < 0 or c > col - 1:
                    continue
                if board[r][c] == "X" or (r,c) in safe:
                    continue
                safe.add((r,c))

                queue.append((r+1,c))
                queue.append((r-1,c))
                queue.append((r,c+1))
                queue.append((r,c-1))

        for i in range(col):
            if board[0][i] == "O":
                bfs(0, i)
            if board[row - 1][i] == "O":
                bfs(row-1, i)

        for i in range(row):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col-1] == "O":
                bfs(i, col-1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"