1. Share questions you would ask to help understand the question:
- Can there be more than 1 rotten orange at the start?
- Is there guarenteed to be a rotten orange or any fresh oranges at all?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Unlikely)

3. Write out in plain English what you want to do: 
- The image that this question draws in my head, is that, in the grid, there are a random placement of rotten oranges, and for every minute, all adjacent fresh oranges are turned rotten. In this one minute, this step happens for every rotten orange. 
- This ressembles BFS, where you kind of expand in all directions, instead of DFS which is only one path
- In this case, a queue can be used like in BFS for a tree. 
- First, traverse through the entire grid to obtain the indexes of all the rotten oranges, as well as keeping a count of the number of fresh oranges found. 
- If, by chance the number of fresh oranges is 0, then return 0
- Else, proceed
- Once all the rotten oranges are obtained, utilize the queue and figure out, by the length of the queue when to detemine that a complete minute has happened
- If by the end of all BFS traversals and the count of fresh oranges is not 0, return -1
- Else, return the number of minutes

4. Translate each sub-problem into pseudocode:
- Intialize a queue for the rotten oranges, an int variable for fresh oranges, and an int for minute count
- Iterate through the whole grid, appending any indexes for rotten oranges to the queue, and incrementing the fresh orange count whenever one is encountered
- Set up a loop that runs until the queue is empty
    - Set up a for loop tha iterates based on the number of rotten oranges in the queue (for example, 2 if at the start, there are only 2 rotten oranges):
        - pop from the left to get a rotten orange
        - check if any adjacent cells have a fresh orange, remebering to not go out of bounds:
            - if there is a fresh orange
                - change value to 2
                - decrement the fresh counter
                - append the index to the queue
            
    - incremenet the minute counter by 1
- if the fresh oranges counter is not 0, return -1
- else, return the minute count

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minute = -1
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0: return 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row > 0 and row < len(grid)) and grid[row-1][col] == 1:
                    q.append((row - 1, col))
                    grid[row-1][col] = 2
                    fresh -= 1
                if (row > -1 and row < len(grid) - 1) and grid[row+1][col] == 1:
                    q.append((row + 1, col))
                    grid[row+1][col] = 2
                    fresh -= 1
                if (col > -1 and col < len(grid[0]) - 1) and grid[row][col+1] == 1:
                    q.append((row, col+1))
                    grid[row][col+1] = 2
                    fresh -= 1
                if (col > 0 and col < len(grid[0])) and grid[row][col-1] == 1:
                    q.append((row, col-1))
                    grid[row][col-1] = 2
                    fresh -= 1

            minute += 1  
            
        return -1 if fresh != 0 else minute -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm utilizes BFS on each rotten orange to simulate the problem
- One weak area are the if statements in the while loop. They can easily be improved by removing the redundant checks which would help performance and readability