1. Share questions you would ask to help understand the question:
- Can there be cases where no 'O's are touching the edges?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- My main takeaway, is that if any 'O' cell is on the edge of the board, performing DFS or BFS on it, all of the cells that are connected to it, can be considered "safe" (since they evantually will connect with a cell that is at an edge)
- Once this is done, any 'O's that are not codsidered safe, will turn into 'X's

4. Translate each sub-problem into pseudocode:
- Intialize a safe set
- create a bfs function that, starting from the current node, appends all connecting 'O's to the safe set
- Iterate through the edges of the board, calling BFS on any cell that is an 'O'

- Then, iterate through the board, and if an 'O' cell is not in the safe set, it is surrounded by 'X's, and thus has to be changed to an 'X'

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
                    board[r][c] = "X" -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that there is no need for already declared safe cells to have BFS performed on them again
- One weak area is that I could have forgone the visited set by switching the calls to queue and only processing O cells. Then I would just change them to a placeholder character so that they don't get traversed again, and then switch them back to "O" as I do that last for,for loop