1. List out any clarifying questions:
- Could a height be negative?

2. List out 1-3 data structures/algorithms that could be useful:
- Two pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The overall problem is to figure out the container that contains the most amount of water
- To first find the max, I need to calculate the amount of water a container can hold
- I would take two heights, calculate their distance as the width, and then multiply that by the lowest height
- The product would be my area
- Instead of checking every potential container size and position, I could just start from both ends of the List
- Then, I just always go to the move the end with the current smallest height
- This way, I am checking only containers that have the potential to be greater, and not every single one

4. Assess the space/time complexity:
- Space: O(1) since I am using constant extra space
- Time: O(n) since I would have to check all of n heights at least once

5. Optional - Give any ways you would improve your solution: