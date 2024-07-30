1. Share questions you would ask to help understand the question:
- Can the matrix be null or empty?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Recursion (Likely)
- BFS (Unlikely)
  
3. Write out in plain English what you want to do: 
- So what this looks like, is that for a soltuion, I can simulate the traversal of a spiral 
- Starting from the outer layer, go in a clock-wise fashion, iterating through the top row, right column, bottom row and left column
- Then when that layer is done, traverse through the next inner layer and repeat, remembering to ensure that the current layer is tracked, so as to not read previous values
- Append the current values throughout the traversals into an output list and return it at the end

4. Translate each sub-problem into pseudocode:
- Initialize an output list 
- Initialize a helper function that will traverse through the layers of the matrix 
- Have its parameters be the length of the row, height of the columns and the current layer
    - Have a base case where there is a single element in the layer 
        - if layer >= the length/2 and >= the height/2
    - Have a for loop that iterates through the layer clockwise
        - row: for i in range(layer, length - layer - 1)
        - column: for i in range (layer, height - layer - 1)
        - append current values to output
    - call the helper function again, but with layer + 1
- Call helper(len(matrix), len(matrix[0]), 0)
- return the output 

5. Translate the pseudocode into Python and share your final answer:
  <!--class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output : List[int] = []

        def helper(row: int, column: int, layer: int):
            if layer >= row/2 and layer >= column/2:
                output.append(matrix[row//2][column//2])
                return

            if len(output) > row * column:
                return

            for i in range(layer, column - layer - 1):
                output.append(matrix[layer][i])

            for j in range(layer, row - layer - 1):
                output.append(matrix[j][column - layer - 1])

            for h in range(column - layer - 1, layer, -1):
                output.append(matrix[row - layer - 1][h])

            for k in range(row - layer - 1, layer, -1):
                output.append(matrix[k][layer])

            if not len(output) == row * column:
                helper(row, column, layer + 1)
                
        helper(len(matrix), len(matrix[0]), 0)
        while len(output) > len(matrix) * len(matrix[0]):
            output.pop()
        return output
 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm is that it can be followed relatively easy, it just goes layer by layer, and traverses in a clockwise traversal
- One weak area is that since I am using the recursion stack, for much larger matrixes, that call stack can get large
- Another would be that there are more conditionals than I would like, that are there to cover edge cases. I would definetly work on this further to remove them