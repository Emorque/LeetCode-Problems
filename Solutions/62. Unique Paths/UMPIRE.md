1. Share questions you would ask to help understand the question:
- Would two paths that share all the same cells except for one that differs, still be considered two unique paths?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- After drawing out a grid myself, and drawing the unique paths, I broke down the problem from "how many unqiue paths to the goal", to "how many unique paths to each cell?
  - Because of that, I realized that the cells in the top row and leftmost col all only have one unique path that leads to them
    - Then, I looked at (1,1), which has two. I did the same for (2,1) which has 3. Then I realized that the get the unique paths of each cell, I can just add the top and left cells together and set it to the current cell
    - After trying this approach, it worked and grid[m-1][n-1] had the correct answer

4. Translate each sub-problem into pseudocode:
- Initializ a grid of m x n, where each value is 1
- Iterating from the (1,1) to the rightmost corner of the grid,
  - set the current cell to the top cell + the left cell

- return the value at grid[m - 1][n - 1]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            grid.append([1] * n)
        
        print(grid)

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[-1][-1] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, by using this grid, I am able to store the number of unique paths that lead to the current cell, which overtime, is used to reach the goal
- One weak area is that without the grid drawn with an example, it may be unclear why adding the cell's top and left neighbor would be the value of the current cell