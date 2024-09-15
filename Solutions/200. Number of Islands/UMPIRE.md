1. Share questions you would ask to help understand the question:
- Is there a chance that there are no islands present?
- Can I edit the grid inplace?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking, is to try using BFS or DFS to, from one piece of land, diverge and note all of the neighboring pieces of land; which in total equate to 1 island
- Since there is no constraint that the grid cannot be edited, changing already traversed pieces of land to something like -1 can make it easy to skip these pieces of land
- So, when one piece of land is found, perform DFS/BFS, and after this traversal is complete, incremenet some count by 1
- Once the entire grid is explored, return output

4. Translate each sub-problem into pseudocode:
- count = 0
- row = len(grid)
- col = len(grid[0])

- def traverse(coordinates): 
  - queue = [coordiantes]
  - while queue:
    - r, c = queue.pop()
    - if r < 0 or r >= row or c < 0 or c >= col:
      - continue
    - if grid[r][c] != "1":
      - continue
    - grid[r][c] == "0"
    - queue.append(r + 1, c)
    - queue.append(r - 1, c)
    - queue.append(r, c + 1)
    - queue.append(r, c - 1)

- for i in range(row):
  - for j in range(col):
    - if grid[i][j] == "1":
      - traverse((i, j))
      - count += 1

- return count

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])

        def traverse(coordinates):
            queue = [coordinates]

            while queue:
                r, c = queue.pop(0)
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if grid[r][c] != "1":
                    continue
                grid[r][c] = "0"
                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    traverse((i, j))
                    count += 1
        
        return count -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm does not use a recursion stack, so it does have good memory usage
- One weak area is that I should have some more explaination as to why I a BFS solution