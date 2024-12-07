1. List out any clarifying questions:
- Is the array sorted?

2. List out 1-3 data structures/algorithms that could be useful:
- Backtracking
- Sorted

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- If I treated this with the normal decision tree, there would be duplicate subsets produced at the end
- However, if I just make sure that I am starting my subset with a unique number each time, I can produce all unique possible subsets
- Since the nums array is not sorted, I can create an outside set to make sure that I don't start a subset with the same number twice
- Then, it becomes a decision tree with 2 decisions at each number
- It isn't working, so I'm thinking it may be easier to just sort the nums list from the start
- Treat it as a 2 decision tree, but skip any duplicate numbers that appear after my current number

4. Assess the space/time complexity:
- Space: O(n*m + 2^n) where n*m is the resulting subsets list for the number of subsets times the average length. 2^n comes from the decision tree where for every n, I do make 2 recursive calls (all numbers are unique)
- Time: O(2^n) for that same reasoning. Also logn for sorting

5. Optional - Give any ways you would improve your solution: