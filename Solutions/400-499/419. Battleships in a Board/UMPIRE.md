1. Share questions you would ask to help understand the question:
- Can the there be multiple battleships within the same row/column?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- Recurions (Unlikely)

3. Write out in plain English what you want to do:
- This question reminds me a lot of the number of islands question. However there is an additional restriction in that the follow-up asks if this can be done without modifying the board
- That does sound tricky, but there is a big difference between battleships vs islands. Battleships are strickly vertical or horizontal, making them rectangles 
- Additionally, battleships cannot be adjacent, so there is no confusion on number of battleships with cases like:
    "X X
     X X
       X" (Are there 3 or 2?)

- Since the entire board needs to be traversed, this be be done from a typical left -> right, up -> down fashion
- So, while traversing, if an 'X' is encountered, If both the top neighbor and left neighbor are water, then it is the front of the ship. Checking top covers vertical battlships and checking left covers horizontal battleships
    - If this false, then the current 'X' is just the body of the battlship
    - If true, then an output variable should be incremented 
- Once traversal is done, return the output

4. Translate each sub-problem into pseudocode:
- Initialize an output int for the result to 0
- Set a for loop to iterate through board's rows:
    - Set a for loop for iterate through that row's columns:
        - If board[row][col] is equal to 'X':
            - If (board[row][col] is at the left edge or board[row][col - 1] is '.') and (board[row][col] is at the top edge or board[row - 1][col] is '.'):
                - increment output by 1
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        output : int = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (j == 0 or board[i][j-1] == ".") and (i == 0 or board[i - 1][j] == "."):
                        output += 1
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm fulfills the follow-up question: Performing with one traversal and not changing values
- One weak area is that it could have better readibility