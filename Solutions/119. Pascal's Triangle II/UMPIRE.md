1. Share questions you would ask to help understand the question:
- What should be returned for 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Bottom-Up (Likely)
- Top-Down (Neutral)

3. Write out in plain English what you want to do:
- A very similar problem to Pascal's Triangle, except a single row is returned instead of the entire triangle
- Therefore, a similar logic can be used, where the curr row's index value is the sum of the previous's rows exact index + that index - 1:
    - row 5[5] = row 4[5] + 4[4]
- A loop can be created that iterates by rowIndex times, and continually does this logic. 
- At the end, return this list 

4. Translate each sub-problem into pseudocode:
- Initialize a List row with [1] * (rowIndex):
    - ex: rowIndex = 5 : [1, 1, 1, 1, 1]
- set up a loop (i) that iterates from (2, rowIndex):
    - set a prev int to row[0]
    - set up another loop (j) that iterates from (1, j):
        - set a temp int to row[j]
        - set row[j] = prev + row[j]
        - set prev to temp 
- return the row list

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            prev: int = row[0]
            for j in range(1, i):
                temp: int = row[j]
                row[j] = row[j] + prev
                prev = temp
        return row -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, in terms of space complexity, the algorithm only uses 0(rowIndex) extra space, that being the row list. The other variables are ints, so constant
- One weak area, is that it could be made more legible, I have two int variables that are handling which number was previous, that can be made more clear.
- I did have to rework a bit of the ranges, since I did not realize that the question wanted 0-indexed. That is my bad, and it was a quick revision. 