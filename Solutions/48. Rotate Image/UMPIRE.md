1. Share questions you would ask to help understand the question:
- What should be handled for empty matrixes?
- Are the values all unique?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Unlikely)
- Recursion (Likely)

3. Write out in plain English what you want to do: 
- What looks like a potential solution is to start the end corners of the matrix, and by using temporary variabales, swap the values at the corners to match a rotated image
- Then move to the next 'corner', so for the top row, that would be the next right element on the x axis, and for the right column, that would be the next down element on the y axis 
- This covers the outermost layer, so if the matrix is have inner layers, some index math needs to be used to recursively go into those inner layers 
- Then once all layers are rotated, return the matrix

4. Translate each sub-problem into pseudocode:
- Make a helper function that takes in the the length of the matrix (number of rows) and the an int to match the current layer 
    - have a base case for when a layer that is 1x1 is hit:
        - if layer >= length/2:
            - return 
    - set up a for loop for iterates through the elements:
        - for i in range (layer, length - 1 - layer): (-1 so as to not hit another corner) (-1 layer to match the current layer)
            - a = matrix[layer][i]
            - b = matrix[i][length - 1 - layer]
            - c = matrix[length - 1 - layer][length - 1 - i]
            - d = matrix[n - 1 - i][layer]
        
            - set the set corners with the temps:
        - call helper again with the same length and layer + 1    
- in the main function, call the helper with len(matrix) and 0
- return  

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(length:int, layer:int):
            print(matrix)
            if layer >= length/2:
                return
            for i in range(layer, length - 1 - layer):
                a : int = matrix[layer][i]
                b : int = matrix[i][length - 1 - layer]
                c : int = matrix[length - 1 - layer][length - 1 - i]
                d : int = matrix[length - 1- i][layer]

                matrix[layer][i] = d
                matrix[i][length - 1 - layer] = a
                matrix[length - 1 - layer][length - 1 - i] = b
                matrix[length - 1- i][layer] = c
            helper(length, layer + 1)
        helper(len(matrix), 0)
        return
                 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that no additional data structures are used, the alogrithm just does its work in-place
- One weak area is that this algorithm is not the most readable. I could have did better labeling to show exactly what each part was doing, such as which row/column was being worked on. 