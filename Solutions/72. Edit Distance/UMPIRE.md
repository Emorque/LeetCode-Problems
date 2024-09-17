1. Share questions you would ask to help understand the question:
- Doesn't this mean that theoretically there is always an answer given, with the worst case replacing characteers in word1 to match exactly with word2, and then deleting the rest
- What are the characters in word1 and word2?
- What are the expected ranges for string lengths?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Neutral)
- DP (Likely)

3. Write out in plain English what you want to do: 
- Drawing out the decision tree, with "horse" as word1 and "ros" as word2, because of the fact that two of the operations negate each other, inserting/deleting, there are times when the same word appears multiple times
  - This immediately brings up the idea of a cache that stores the minimum distance for each edited word, so that it can be referenced without repeating already done work
  - Then there are also some edge cases when deciding on if some operations should happen
    - if word1 + a character has a greater length than word2, don't insert a character (This would go on forever)
    - if word1 - a character has a length less than word 2, don't remove
    
    - In both cases, just do the opposite operation and replace

- After some time with a 2d array, I think I know what the operations would look like on this array:
  - if the characters match, set the right,down diagonal neighbor by self, no operations needed
  - inserting: incrementing the down neighbor by self + 1
  - delete: increment the right neighbor by self + 1
  - replacing: incrementing the right,down diagonal neighbor by self + 1

- So, just like with a DFS approach, I can start from the rightmost downmost cell and then traverse from right -> left, bottom->right, using the logic explained above
  - EXCEPT, the current cell is what changes, not the neighbors. The neighbor's values are used to set the current cell. 
  - Checking all neighbors if the characters don't match, and set the current self to the min of them
  - If they do match, set the current self to the 
- Then in the end, I return grid[0][0] to right,down diagonal neighbor

- And one last thing, there needs to be an extra row and column to do some of these neighbor checks, and it would be:
  - from the current len of the respective word and decrease going right/down
  - ex: 3, 2, 1, 0

4. Translate each sub-problem into pseudocode:
- initailize a 2d cache array, with each value set as len(word1) + len(word2), realistically, there should be no reason for there to be more operations than that
- Set the right most col and set it from top, down in descending order
- Set the bottom most row and set it from left, right in decending order
  - Both of which start from the length of its respective word

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid = []
        mostOperations = len(word1) + len(word2)
        for i in range(len(word2)):
            grid.append([mostOperations] * (len(word1) + 1))
            grid[i][-1] = len(word2) - i
        
        lastRow = []
        for j in range(len(word1) + 1):
            lastRow.append(len(word1) - j)
        
        grid.append(lastRow)

        for r in range(len(grid) -2 , -1, -1):
            for c in range(len(grid[0]) - 2, -1, -1):
                if word1[c] == word2[r]:
                    grid[r][c] = grid[r + 1][c + 1]
                else:
                    grid[r][c] = min(grid[r + 1][c] + 1, grid[r][c + 1] + 1, grid[r + 1][c + 1] + 1)

        return grid[0][0] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution uses a Bottom-Up DP approach, built from the logic of that dfs approach. Because of that, there is a more efficient use of space, then recursively calling up to 3 times in each call
- One weak area is that this solution can be improved further, and that is, since after some time, previously traversed rows are no longer used for computations. So, 2 arrays can be used instead of len(word2) or len(word1) rows (depending on how the grid is created)