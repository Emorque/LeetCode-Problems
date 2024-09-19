1. Share questions you would ask to help understand the question:
- What is the expected range for the m and n in matrix?
- What is the expected range that each element in the matrix can be?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 
- I thought a good solution would be to store each row and col that needs to be converted in a set
- But, then I realized that since I am going to be turning this row and col in a 0 anyways, why not set them now? What I mean is to set the leftmost cell and topmost cell of the current cell if it equals to 0.
- Since I am traversing from left -> right, top -> bottom, I dont have to worry about these new 0s being seen as 0s from the original matrix
- Then I just traverse through the top row and the bottom and if I see a zero, set zeros to the entire row/col 

4. Translate each sub-problem into pseudocode:


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        topRow = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        topRow = True
                    else:
                        matrix[r][0] = 0
                        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if topRow:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that no extra space is used for anything, just that fact that cells that were already going to turn into a 0, is used as a flag for future reference
- One weak area is that in persuit of this O(1) space, there is a lot of passes through the matrix