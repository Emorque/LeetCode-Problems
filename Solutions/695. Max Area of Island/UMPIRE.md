1. Share questions you would ask to help understand the question:
- Can there be 0 islands in a test case?
- What is the grid is empty?
- Can I edit the grid?
- Are the elements ints?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking of, is implementing a kind of BFS/DFS approach, where for every "1" I come across, I enter BFS or DFS and traverse all of the neighboring pieces of land
- If the current coordinate I am in is a piece of land, I can incremenet some count by 1
- Once I've traversed all the pieces of land, I can return that count variable, and in the outer function, I'll keep track of the max area by using max() 

4. Translate each sub-problem into pseudocode:
- Initialize maxArea to 0
- Get the row and col size of the grid

- def traverse(coordiantes) -> int:
  - area = 0
  - queue = [coordiantes]

  - while queue:
    - r, c = queue.pop(0)

    - check if coordinates are valid:
    - if r < 0 or r >= row or c < 0 or c >= col:
      - continue
    - if grid[r][c] != "1"
      - continue
    - Now, we are currently on land
    - groud[r][c] = 0
    - count += 1 
    - append all four neighbors into the queue
  - return count

- for i in range(row):
  - for j in range(col):
    - if grid[i][j] == 1:
      - maxArea = max(maxArea, traverse((i, j)))

- return maxArea


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row = len(grid)
        col = len(grid[0])

        def traverse(coordinates) -> int:
            area = 0
            queue = [coordinates]

            while queue:
                r, c = queue.pop(0)

                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if grid[r][c] != 1:
                    continue
                grid[r][c] = 0
                area += 1
                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))
            
            return area
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, traverse((i, j)))
        
        return maxArea
                 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses an efficient BFS, by implementing a queue, and just returning the area of the island we area currently on
- One weak area is taht some comments can help break down this solution into more digestible parts