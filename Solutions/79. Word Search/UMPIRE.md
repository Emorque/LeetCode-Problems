1. Share questions you would ask to help understand the question:
- Does the order of characters in word need to be maintain?
    - For example, what if word is "for", and there are strings: "o" "f" "r" in matrix.
        - What should be returned?
- Can word be a longer word than there are avialable letters in the board?
- Can I edit the board inplace?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking of, is trying out a DFS helper function, that will begin once the first letter in word is found. 
- Then, check all four adjecent cells and see if the next word can be found. The current cell should be appended to a set so that it cannot be considered in the next call. Then afterwords, it can be removed

4. Translate each sub-problem into pseudocode:
- initialize a coordinates set

- create dfs helper(currCell, currIndex):
    - if currCell in set or row == rowSize or row < 0 or col == colSize or col < 0 or board[row][col] != word[currIndex]:
        - return False
    - if currIndex == length(word) - 1:
        - return True
    - coordinates.add(currCell)

    - found = dfs((row - 1, col), currIndex + 1) or dfs((row + 1, col), currIndex + 1) or dfs((row, col - 1), currIndex + 1) or dfs((row, col + 1), currIndex + 1)
    
    - coordiantes.remove(currCell)

    - return found

- iterate through the rows and columns:
    - if the word[0] is found:
        - coordinates.add((i, j))
        - if dfs((i,j), 1); 
            - return True
        - coordiantes.remove(i,j)
- return False

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
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
        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- The strong area about this alogrithm is that a set is used to quickly insert and remove coordiantes from the current path. And is able to be used to ensure previously traveled coordinates are not traveresed again 
- And a backtracked logic is used to let each dfs call have its own set 
- The weak area is the volume of long lines of code, that should certainly be reworked