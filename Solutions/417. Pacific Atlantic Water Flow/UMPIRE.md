1. Share questions you would ask to help understand the question:
- Does the list needed to be in a certain order?
- Can there be negative heights?
- Are the cells in the top right and bottom left always flowing into both oceans?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking of, is using a BFS so that for each time queue is iterated, we branch equally from one cell, as oppposed to DFS where we kind of commit to one path at a time
- Within the BFS, I will use two booleans, one for each ocean, and if both oceans are hit, then those booleans turn true
- I also had an interested idea, where if one cell does reach both oceans, then that one can be considered special. In future BFS's of other cells, if it reaches a cell that has reached the ocean, then we know right away that that cell will reach both oceans. 

4. Translate each sub-problem into pseudocode:
- Intialize and an output list
- Iterate through the heights list
- For each cell, perform BFS
  - if that cell reaches both oceans, return True and add it to a marked set 
- return the output list

- BFS:
  - starting from the queue, only append neighboring nodes if they are <= the current cell
  - set booleans for each ocean, and set them to true if a cell is touching them
  - if the queue is done and neither booleans are true, return False

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        marked = set()

        def bfs(coordinates) -> bool:
            pacific, atlantic = False, False
            visited = set()
            queue = [coordinates]
            
            while queue:
                r, c = queue.pop(0)
                if r == 0 or c == 0:
                    pacific = True
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    atlantic = True
                if pacific and atlantic or (r,c) in marked:
                    return True
                if (r, c) in visited:
                    continue

                visited.add((r,c))

                if r > 0 and heights[r - 1][c] <= heights[r][c]:
                    queue.append((r - 1, c))
                if r < len(heights) - 1 and heights[r + 1][c] <= heights[r][c]:
                    queue.append((r + 1, c))

                if c > 0 and heights[r][c - 1] <= heights[r][c]:
                    queue.append((r, c - 1))
                if c < len(heights[0]) - 1 and heights[r][c+1] <= heights[r][c]:
                    queue.append((r, c + 1))
            return pacific and atlantic 
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs((i, j)):
                    output.append([i, j])
                    marked.add((i,j))
        
        return output
         -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it does use a set to mark successful cells, which saves some processing
- One weak area is that BFS is performed for each cell, which does get very costly, even with the marked set. There is a way to save some time further
  - For example, if the cell was not able to return True in bfs, then every cell that was in it's path cannot be starting cells (they will never reach both oceans if they are the start of a bfs)
  - This however, requires another data structure which I would do I if I were to continue with this solution

- A more efficient solution would be to start from the cells that I know cross one of the oceans, and then perform BFS from them to cells that are at greater heights, since the inverse of flowing from a cell down to the ocean, is to go from the ocean up to a cell
  - Then cross examine the cells from the ocean's set of cell, and see if any cells are in both sets. Those cells are confirmed to be able to flow into both oceans
  - This is much simplier and saves a lot of time as cells don't have to be retraversed
  - This solution is in the py file too