1. List out any clarifying questions:
- Is it sorted in any way?

2. List out 1-3 data structures/algorithms that could be useful:
- Sorting
- Backtracking

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- If I can be sure that the candidates array is sorted, then I can just skip any potential duplicate numbers 
- This also helps as if I come across a single number that is greater than the target, I can stop creating combinations as any future numbers will always be greater than target, hence won't be in any valid combinations
- So I can have a loop to create my starting combinations. 
- I'll skip any numbers I've seen 
- Then in a helper function, I'll simulate a decision tree, with the base case being that the sum of my combination == target. Then I can add this to my collection of combinations

4. Assess the space/time complexity:
- Space: O(2^n + n*m) as I would explore 2 paths for each n if in the worst case scenerio, with n*m being the combinations list. n for the number and m for the average length
- Time: O(2^n) for the same reason as above

5. Optional - Give any ways you would improve your solution: