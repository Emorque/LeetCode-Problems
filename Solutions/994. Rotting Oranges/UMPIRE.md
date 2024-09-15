1. Share questions you would ask to help understand the question:
- There is a chance that an orange has no neighboring rotten oranges ever?
- Can there be a case where no rotten oranges exist?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Unlikely)

3. Write out in plain English what you want to do: 
- Since every minute, a rotten orange affects the neighboring cells, something like BFS would be more applicable, since every minute, I can kind of branch out from each rotten orange
- If I were to use DFS, then I would go down one route, not necessarily all four directions as efficiently as BFS
- To start off, I would need to get the coordinates of all the rotten oranges, and the number of fresh oranges
- Then, put each one into a queue, and run BFS until that queue is empty. 
- Every time I turn a fresh orange rotten, decrement the fresh count by 1
- At the end, return the time if fresh count is 0, else return -1 

4. Translate each sub-problem into pseudocode:
- Initialize a fresh count, timer
- Initialize a queue

- iterate through the grid, and append the coordiantes of all rotten oranges into the queue 
    - if a fresh orange is found, increment that count by 1

- then set up a loop that iterates while queue:
    - for i in range(len(queue)):
        - rotten = queue.pop(0)
        - if rotten != 1 or is out of bounds
        - continue
        - grid[rotten] = 2
        - fresh -1
        - append neighboring cells into queue
    - timer += 1

- return timer if fresh == 0 else -1

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, timer = 0, 0
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return timer
        
        while queue:
            for k in range(len(queue)):
                r, c = queue.pop(0)
                if r > 0 and grid[r - 1][c] == 1:
                    queue.append((r - 1, c))
                    grid[r-1][c] = 2
                    fresh -= 1
                if r < len(grid) - 1 and grid[r + 1][c] == 1:
                    queue.append((r + 1, c))
                    grid[r+1][c] = 2
                    fresh -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    queue.append((r, c - 1))
                    grid[r][c-1] = 2
                    fresh -= 1
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2
                    fresh -= 1
            timer += 1
        
        return timer - 1 if fresh == 0 else -1 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a loop first checks the size of the queue, so that for the current minute, only the oranges that are in the queue get processed
- One weak area is that the four neighbors to need to be checked first which does lead to the lengthly if statements above