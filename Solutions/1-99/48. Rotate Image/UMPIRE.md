1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I think one way of going about this, is to think of the problem like:
    - Take the four corners of the matrix, swap them with each other, and then look at the next corners to swap (clockwise orientation)
    - I can consider the boundaries the same for all four sides the same, since this is an nxn matrix, a square
    - Then to look into the next inner layer, I just decrement the boundaries by 2
- I can do this with a left and right pointer, and have my for loop iterate through their difference, and after, have them go towards each other
- Since a nxn matrix stops being rotated when the layer has no other layer within or is a single cell, I can stop once left == right

4. Assess the space/time complexity:
- Space: O(1)
- Time: O(n^2)

5. Optional - Give any ways you would improve your solution: