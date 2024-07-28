1. Share questions you would ask to help understand the question:
- Are the only values '0' and '1'?
- Are there always islands?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Likely)

3. Write out in plain English what you want to do: 
- So this seems like a minor step ahead of the numIslands problem
- So, a similar algorithm can be used
- In numIslands, all that I was concerned with was finding island and returning the count
- Now, I have to consider the amount of 'nodes' that are in the island and keep a count
- So, a traversal function can be used whenever 1 is found.
  - Just before it is first called, a curr counter should be set to 0.
  - Then everytime the traversal function is called, increment this curr value
  - Once all the calls have been made, set the output to the max between itself and curr
- repeat this until the entire grid is traversed and then return the output

4. Translate each sub-problem into pseudocode:
- initialize a row and column size with len(grid) and len(grid[0]) respectively
- initialize an output to 0
- initialize a value curr to 0
- then, iterating through the rows and columns
- once I reach a '1':
  - set curr to 0
  - Call a helper function that branches from it and turns any adjacent '1's into '0's
    - increment curr everytime
  - after the recursion stack is done, set output to max(output, curr)
- return the output

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        output = 0
        curr = 0

        def traverse(i: int, j: int):
            grid[i][j] = 0
            nonlocal curr
            curr += 1
            if i + 1 < row and grid[i + 1][j] == 1:
                traverse(i + 1, j)
            if i - 1 > -1 and grid[i - 1][j] == 1:
                traverse(i - 1, j)
            if j + 1 < column and grid[i][j + 1] == 1:
                traverse(i, j + 1)
            if j - 1 > -1 and grid[i][j - 1] == 1:
                traverse(i, j - 1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    curr = 0
                    traverse(i, j)
                    output = max(output, curr)

        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm branches from any '1's to find any neighboring land, and does so in-place
- One weak area is that a recursion stack is used, which could balloon if the grid gets really large