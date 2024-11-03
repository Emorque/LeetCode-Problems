1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Backtracking 
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Ideally I would start with 1, and then work through some n number paths that each are if I choose one of the rest of the numbers as the next number to add to my permutation
- In order to record whether I have seen some number before, I'll use a set to record all current numbers in my permutation. This is only possible because the nums list only has unique numbers
- So I'll use a helper function that passes in its current permutation, and then I'll have an outer set that records the currently appended numbers
- Once a path is explored, I'll both pop that number from the permutation and remove it from my set

4. Assess the space/time complexity:
- Space: O(n * n! + n) the lone n is from the set and n * n! coems from the storage of all the permutations
- Time: O(n * n!) as for the size of n, I end up prodoucing n! permutations 

5. Optional - Give any ways you would improve your solution:
- Seeing other solutions, I realized that while the set does work, it is still the same time complexity as just exploring the current permutation for a number. All without the need of an extra data structure