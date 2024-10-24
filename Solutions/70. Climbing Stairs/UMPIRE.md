1. List out any clarifying questions:

2. List out 1-3 data structures/algorithms that could be useful:
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- After drawing staircases with 1-4 steps, it looked like whatever staircase I was looking at, the answer was the sum of the two previous staircases
- It works for these examples, but I got stumped for a bit figuring out why this works logically so that it can be applied to larger staircases
- I then realized, that it has to do with the first step that is taken. If I climb one step, then the remaining steps are n-1, and if I climb two steps, then the remaining steps becomes n-2. Since these are my only two possible starting points, summing the answers of n-1 and n-2 would give me all combinations. 
- So what I'll do is have two ints, since I need to remember my previous two staircases. Any more before that is not neccessary 
- My base should be 1, as one step can only be climbed one way. I can create a loop that iterates n times, that results in the second int representing the current value of n. 

4. Assess the space/time complexity:
- Space: O(1) since I can just using 2 extra int variables
- Time: O(n) as I need to compute my while loop n times

5. Optional - Give any ways you would improve your solution: