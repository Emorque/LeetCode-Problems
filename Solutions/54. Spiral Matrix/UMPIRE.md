1. Share questions you would ask to help understand the question:
- Can there be a case with either m and n are both 1?
- What are the ranges that m and n can be?
- Are the values all distinct?
- By spiral, do you mean clockwise and then going into the next inner layer?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 
- Get the number of cols and rows and do the top most layer, making sure to not recheck already seen elements
- Then go into the next layer, with a new set of boundaries

4. Translate each sub-problem into pseudocode:
- Set up the left, right and top, bottom boundaries of the grid
- Then as I complete a row and col, readjust the boundaries 
- Once the boundaries have all overlapped, the entire grid is traversed
- Or in the loop, if either of the boundaries have overlapped (are equal), then output can be returned

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        output = []

        while left < right and top < bottom:
            # top Row
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            # right Col
            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                return output
            
            # bottom Row
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][i])
            bottom -= 1

            # left Col
            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it breaks the problem into a smaller problem of getting dealing with the matrix at one layer at a time
- One weak area is that there is some repeated elements in the code