1. Share questions you would ask to help understand the question:
- Does that mean that either or both strings can have nothin in them?
- In the case of which there are no common subsequences, even with individual letters, do I return 0?
- What characters can I expect in with string? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)

3. Write out in plain English what you want to do: 
- After some trial and error, sorting the words against each other on a grid helped to visualize a solution. In a weird way I thought of the Pokemon type chat, where the value of the current cell is dependent on what the x, y values represent.
  - In this case, that would be if at index x for word 1 and index y for word 2, is there a match?
  - If there is, I want to set its value to 1 plus what is diagonally left-up to it.
  - The reason is that there is now a senerio where we are building a common subsequence. 
    - If there is no match, then set the current cell to the max of its top and left neighbor. 
    - Since the base case of this solution is 0 (there is no common subsequence), once at least one is found, we can carry that on to the path of every character beyond that cell.
      - If is a bit hard to explain without my drawing, but basically, once a match is found, that means we can split the words after their current indexes, and from there on, there is at least a subsequence of length 1 onward. This length grows as more matches are found
- Then at the end, return the right most, down most cell

4. Translate each sub-problem into pseudocode:
- Initialize a grid will zeros of length text1, and height text2 with an extra row and col. With each cell starting at 0 (base case)

- Iterate from index 1 to the end of the row
  - interate from index 1 to the end of the col
    - if the characters match:
      - current cell = 1 + [row - 1][col - 1] cell
    - else
      - current cell = max(top neighbor, left neighbor)

- return the grid[len(text1), len(text2)]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = []
        for i in range(len(text2) + 1):
            grid.append([0] * (len(text1) + 1))
        
        for r in range(1, len(text2) + 1):
            for c in range(1, len(text1) + 1):
                if text2[r - 1] == text1[c - 1]:
                    grid[r][c] = 1 + grid[r - 1][c - 1]
                else:
                    grid[r][c] = max(grid[r-1][c], grid[r][c-1])
        
        return grid[len(text2)][len(text1)] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution uses a 2d grid to store the current longest common subsequence. The moment that the lengths of two subsequences differ, only the max one carries on
- One weak area is that without the visualization, it isn't clear that the "grid[r][c] = 1 + grid[r - 1][c - 1]" is there because, once a character matches, we now only consider the substrings of the words after their match