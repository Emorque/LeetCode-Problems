1. Share questions you would ask to help understand the question:
- Will numsRow be positive?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bottom-up (Likely)
- Top-down (Likely)

3. Write out in plain English what you want to do:
- Pascal's Triangle looks interesting, drawing it, I realized that when calculating the number on a cell that is not at the edge, it is the sum of that index and the previous index in the previous row
- As an example, for row 3, the index [1] is the sum of row 2's indexes [1] and [0]
- Using this log, a loop can be created that iterates through the numsRow
    - As each iteration, build a new row that is the length of that row (ex: row 5 has 5 elements)
    - Then, use the logic explained previously
- Once that triangle is completed, return it

4. Translate each sub-problem into pseudocode:
- Initialize an output to: [[1],[1,1]]
- if numsRow is 1: return [[1]]
- Set a for loop that iterates from (2, numsRow):
    - create a newList that is [1] * (i + 1)
    - set another loop that iterates from (1, length(newList)-1)
        - newList[j] = prevList[j] + prevList[j-1]
    - append the newList to output
- return output  


5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        output = [[1], [1,1]]
        for i in range(2, numRows):
            newList = [1] * (i + 1)
            for j in range(1, len(newList) - 1):
                newList[j] = output[i-1][j] + output[i-1][j-1]
            output.append(newList)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it mimics the animation and uses the logic: for a cell that is not at the edge, it is the sum of that index and the previous index in the previous row
- One weak area is that it could be optimized to not have output initialized to [[1],[1,1]]