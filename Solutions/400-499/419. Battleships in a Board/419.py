from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        output : int = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (j == 0 or board[i][j-1] == ".") and (i == 0 or board[i - 1][j] == "."):
                        output += 1
        return output