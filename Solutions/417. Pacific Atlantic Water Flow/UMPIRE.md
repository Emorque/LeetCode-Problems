1. Share questions you would ask to help understand the question:
- Can there be multiple paths that a cell can take to reach the oceans?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)
- BFS (Likely)

3. Write out in plain English what you want to do:
- One of the things that I realized that I want to try to incorporate is this logic:
  - Starting from the current cell, if after traversing through neighboring cells, that current cell does not reach the Pacific and Atlantic oceans, then I know that all visited cells also DO NOT reach both oceans
  - This can be broken up into the following problems:
    - Starting from the current cell, how can I reach both oceans that know that I have hit both?
    - How can I document visitied cells from that journey?
  - A helper function utlizing DFS can be used
  - Using recursion, the starting cell will branch off and all visited cells will be kept in a currently visited set.
    - If both oceans are reached, append the starting cell to the output
    - If not, append all cells that were in the currently vistied set to a all visited set (cells here do not need to be retraversed)
  - return the output list 

4. Translate each sub-problem into pseudocode:
- Initialize a output list, and a visited set
- have two booleans: one for each ocean starting at False
- initialize a currently visiting set
- create a helper dfs function, that takes in two parameters, current cell and starting cell
  - use recursive dfs to traverse:
    - if current cell in currently visited or visited or (pacfic and atlantic):
      - return
    - if current cell[0] or cell[1] == 0: set pacific to true
    - if current cell[0] == len(heights-1) or cell[1] == len(heights[0]-1): set atlantic to true;
    - if both booleans are true,
      - append the starting cell to the output list
      - add starting cell to visited set
      - return 
    - call dfs on all four neighbers
  - create for loop that iterates through the rows and columns:
    - call dfs on the current cell
    - once returned:
      - if both booleans are true:
        - set both to false
      - else:
        - append the currently visited set to the visited set (for i in loop)
  - return the output list
    
5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output: List[List[int]] = []
        currVisited = set()
        pacific, atlantic = False, False
        rows =  len(heights)-1
        columns = len(heights[0])-1

        def dfs(currCell: List[int], startCell: List[int]):
            nonlocal pacific
            nonlocal atlantic
            i = currCell[0]
            j = currCell[1]
            if (i,j) in currVisited or (pacific and atlantic):
                return
            if currCell[0] == 0 or currCell[1] == 0:
                pacific = True
            if currCell[0] == rows or currCell[1] == columns:
                atlantic = True
            if pacific and atlantic:
                output.append(startCell)
                return
            currVisited.add((i,j))
            if i > 0 and heights[i][j] >= heights[i - 1][j]:
                dfs([i-1, j], startCell)
            if i < rows and (heights[i][j] >= heights[i + 1][j]):
                dfs([i+1, j], startCell)

            if j > 0 and heights[i][j] >= heights[i][j-1]:
                dfs([i, j-1], startCell)
            if j < columns and heights[i][j] >= heights[i][j+1]:
                dfs([i, j+1], startCell)
        for i in range(rows+1):
            for j in range(columns+1):
                dfs([i,j], [i,j])
                pacific, atlantic = False, False
                currVisited = set()
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that any visited cells in the current dfs are not retravered
- One weak area is that my initial plan of having a global set of cells that were detemined to not be able to reach any ocean (my logic from #3) did not work. I likely could have incorporated it if I had worked on it more, but I am glad that I at least have a currVisited set. 
- Another weak area is that, since recursion is used, this algorithm will be slowly than if a queue and BFS were used