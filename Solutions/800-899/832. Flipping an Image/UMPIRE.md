1. Share questions you would ask to help understand the question:
- Will there be any empty test cases?
- Will there be any values other than 0 or 1?
- Can the rows have unique lengths?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointers (Likely)
- BFS (Unlikely)

3. Write out in plain English what you want to do: 
- The instructions were laid out in the description.
- How I can go about this question can be:
  - Iterate through the rows, reversing the values
  - While doing this, invert the current values 0 -> 1 and 1 -> 0
- return the image

4. Translate each sub-problem into pseudocode:
- set up a for loop that iterates through the lists
- set up another for loop that iterates through the ints
    - set up a pointer at the start of the list and one and the end
    - set up a while loop that iterates until the two pointers intersect
        - swap the values at the pointers
        - invert the values of the pointers
        - move p1 by 1 and p2 by 1

6. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if len(image) == 1:
            image[0][0] = 0 if image[0][0] == 1 else 1
            return image
            
        for i in range(len(image)):
            p1 = 0
            p2 = len(image[i]) -1
            while p1 < p2:
                image[i][p1], image[i][p2] = image[i][p2], image[i][p1] 
                image[i][p1] = 0 if image[i][p1] == 1 else 1
                image[i][p2] = 0 if image[i][p2] == 1 else 1 
                p1 += 1
                p2 -= 1
                if p1 == p2:
                    image[i][p1] = 0 if image[i][p1] == 1 else 1
                    break
        return image -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the solution does the work in-place
- Another is that the this it is handled in one traversal of the image
- One weak area is that I think it could be written better to not have that first if statement and inner if statement in the while loop
    - It hurts readability and handle edge cases 