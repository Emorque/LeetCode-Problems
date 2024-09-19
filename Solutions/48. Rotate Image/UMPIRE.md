1. Share questions you would ask to help understand the question:
- What is the range of numbers that each number in the grid can be?
- What is the range that n can be in?
- Are the values distinct?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Math

3. Write out in plain English what you want to do: 
- Determine the number of times I am switching the numbers at each level (starting at n - 1)
- Then I will set four pointer at each corner, set their numbers to temp variables and then resetting them to their respective temps
- move the pointers accordingly
- Once thats done, subtract that numbers at each level by 2 for the next level, and move the pointers to the inner layer

4. Translate each sub-problem into pseudocode:
- We want to traverse n//2 layers
- The number of times we want to rotate cells in a layer is layer - 1

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        layer = len(matrix) // 2
        swaps = len(matrix) - 1
        edge = len(matrix) - 1 

        for i in range(layer):
            for j in range(swaps):
                topL = matrix[i][i + j]
                topR = matrix[i + j][edge]
                bottomR = matrix[edge][edge - j]
                bottomL = matrix[edge - j][i]

                matrix[i][i + j] = bottomL
                matrix[i + j][edge] = topL
                matrix[edge][edge - j] = topR
                matrix[edge - j][i] = bottomR

            edge -= 1
            swaps -= 2 -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm is just the literal implementation of grabbing each corner element and then setting them accordingly, and then going inside one layer
- One weak area is that there is a more efficient solution that is by doing a transpose, followed by a reversal. Something neet to know that equates to this rotation, which makes coding it easier