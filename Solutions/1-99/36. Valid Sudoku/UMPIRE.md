1. List out any clarifying questions:
- What is in a blank cell?

2. List out 1-3 data structures/algorithms that could be useful:
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I'm looking to make sure that the board is valid by ensuring there is no repetion in any squares, rows, and cols, a set would be great. Each row, col, and square would have its own set, and so if I find a number in a row set that already exists, I know that the board in invalid
- The thing is that I would have to then have 27 sets for each possible row, col, and square
- Manaully setting each one seems unrealistic, so I think I can use 3 dictionaries, one for rows, cols, and squares. The keys can be numbered 1-9. So like (4,3) on the board would be row 4, col 3. 
- So to determine the current square, something I can do is divide the x and y cord by 3. Becuase there are 9 rows and 9 cols, so by dividing that by 3, I get 9 perfect square sections. The top left square would be (0,0) and the bottom right would be (2,2)

4. Assess the space/time complexity:
- Space: In the worse case scnerio were all cases are filled, and I need to process all of them, there will be 3 dictionaries with 9 keys each, each of which have a set of size 9. Since its constant no matter the board, space goes from O(81) (for 81 cells), to O(1)
- Time: The same logic applies to time. I process each cell, so since there are 81, time goes from O(81) to O(1)

5. Optional - Give any ways you would improve your solution: