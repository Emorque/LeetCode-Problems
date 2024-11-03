from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        row = len(board)
        col = len(board[0])

        def helper(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            if board[r][c] != word[index] or (r,c) in visited:
                return False

            visited.add((r,c))
            
            found = helper(r + 1, c, index + 1) or helper(r - 1, c, index + 1) or helper(r, c - 1, index + 1) or helper(r, c + 1, index + 1)

            visited.remove((r,c))
            return found
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    # visited.add((i,j))
                    print("entered")
                    if helper(i, j, 0) == True:
                        return True
                    # visited.remove((i,j))
        return False