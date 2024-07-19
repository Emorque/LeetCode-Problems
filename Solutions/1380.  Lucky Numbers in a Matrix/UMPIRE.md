1. Share questions you would ask to help understand the question:
- Can there be more than one lucky number in a case?
- What should be returned for null test cases?
- Can there be a test case where there is just one column and >1 rows or vice versa?
- Are the matrixes all always perfect rectangles?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Matrix (Likely)
- Set (Likely)

3. Write out in plain English what you want to do: 
- So what is needed is to find out if there are any numbers that are both the min in their row and the max in their column
- How this could be done is by iterating through the matrix
- Add the min in the row to a set and the max in the column to the same set
- If there is every a time when a duplicate is trying to be added:
- Append that number to the output list 

4. Translate each sub-problem into pseudocode:
- Initialize a set to hold all the mins and maxs
- Initialize a list to be the output 
- Set a for loop and an inner for loop that will iterate through the matrix by the row and columns:
    - For the row, find the min and add it to the set 
    - For the column, find the max and add it to the set 
    - If a number is to be added to the set that is already in the set, add it to the output list 
- return the output list

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minAndMax = set()
        output = []
        # get the mins
        for i in range(len(matrix)):
            minimum = 1000000
            for j in range(len(matrix[i])):
                minimum = min(minimum, matrix[i][j])
            minAndMax.add(minimum)
        #get the maxes
        for i in range(len(matrix[i])):
            maximum = 0
            for j in range (len(matrix)):
                maximum = max(maximum, matrix[j][i])
            if maximum in minAndMax:
                output.append(maximum)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that since the values in the matrix are all distinct, the set only needs to contain the mins to compare to the maximums
- One weak area is that the algorithm needs to iterate through the entire matrix twice, to get both the mins and the maxes 
    - If I were to rework this, my first goal would be to see if it were possible to get the most out of one pass