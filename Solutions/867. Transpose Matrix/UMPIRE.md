1. Share questions you would ask to help understand the question:
- Are the given matrix squares? As in the width is equal to the height?
- Can this be done in-place?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- BFS (Unlikely)
- Inplace (Neutral)

3. Write out in plain English what you want to do: 
- Given the definition of what transpose means and the given the image, transposing seems to mean that rows bcomes columns and vice versa
- So what could be done, is that I either traverse row by row or column by column, and then append it as the opposite thing in a new matrix

5. Translate each sub-problem into pseudocode:
- Initialize an output list of ints in a list
- Iterate through the input matrix by its columns, appending every value into a list
    - Append this list as a row to the output list
- return the output list

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output: List[List[int]] = []

        for i in range(len(matrix[0])):
            entry : List[int] = []
            for j in range(len(matrix)):
                entry.append(matrix[j][i])
            output.append(entry)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the algorithm makes use of the how a transpose is defined to only need to traverse through each element one
- One weak area is how I set up the output and append values. I could have set up a output with a set length and height and then set the values in the loop, instead of appending.