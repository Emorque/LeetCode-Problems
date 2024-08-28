1. Share questions you would ask to help understand the question:
- Are the values unique?
- Is the matrix a perfectly shaped rectangle?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Binary Search (Likely)
- Two pointer (Likely)

3. Write out in plain English what you want to do: 
- Since the numbers are all in ascending order the the first number of a row is always greater than the last of a previous row, binary search can be used on the first numbers of each row 
- Once the left and right pointers intersect, that means the current row has to have the target in it \
  - There could also be another check, where if the target is the first number in a row, the answer can be returned then 
- Now, perform binary search on that row until the target is found
- If the pointers intersect and nothing has been returned, return false
- Else, true

4. Translate each sub-problem into pseudocode:
- Binary search with the rows:

- Set low to 0, and high to the number of rows
- While low <= high:
  - mid = low + (high - low) // 2
  - if mid[0] == target: return True
  - else if mid[0] < target
    - low = mid + 1 
  - else:
    - high = mid - 1

- current row = high 

- set l to 0, and h to length of matrix[high]
- While l <= h:
  - mid = l + (h - l) // 2
  - if matrix[high][mid] == target: return True
  - else if mid[0] < target
    - low = mid + 1 
  - else:
    - high = mid - 1
- return False

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] == target: 
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        # current row is high 
        
        l, h = 0, len(matrix[high]) - 1

        while l <= h:
            mid = l + (h - l) // 2

            if matrix[high][mid] == target: 
                return True
            elif matrix[high][mid] < target:
                l = mid + 1
            else: 
                h = mid - 1
        return False -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it performs binary search on both the rows and then the individual row itself, with a time complexity of: O(log(m) + O(log(n))
- One weak area is that I think another check can be used before the second binary search, where if the end of the high row is less than the target, return False
  - This means that while target fits this row based on the first number, if the end of the row is less, than the target is out of the range, so False can be returned earlier