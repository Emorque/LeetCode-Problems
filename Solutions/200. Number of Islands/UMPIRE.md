1. Share questions you would ask to help understand the question:
- Are the only potential values '0' and '1'?
- What is the area outside of the grid?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Likely)


3. Write out in plain English what you want to do: 
- This grid resembles a big map or web of nodes
- So thinking like that, I could traverse through each 'node' and when I reach one with a value of '1':
  - I edit it to a different value like '0' and then traverse to adjecent 'nodes' until I hit '0' for all of them
  - Then I would increment my output variable by 1
- After traversing through the whole grid, I return that output

4. Translate each sub-problem into pseudocode:
- initialize a row and column size with len(grid) and len(grid[0]) respectively
- initialize an output to 0
- then, iterating through the rows and columns
- once I reach a '1':
  - I would call a helper function that branches from it and turns any adjacent '1's into '0's
  - increment the output
- return the output


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        output = 0

        def traverse(i: int, j : int):
            grid[i][j] = '0'
            if i + 1 < row and grid[i+1][j] == '1':
                traverse(i+1, j)
            if i - 1 > -1 and grid[i-1][j] == '1':
                traverse(i-1, j)
            if j + 1 < column and grid[i][j+1] == '1':
                traverse(i, j+1)
            if j - 1 > -1 and grid[i][j-1] == '1':
                traverse(i, j-1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    output += 1
                    traverse(i,j)

        return output-->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm branches from any '1's to find any neighboring land, and does so in-place
- One weak area is that a recursion stack is used, which could balloon if the grid gets really large