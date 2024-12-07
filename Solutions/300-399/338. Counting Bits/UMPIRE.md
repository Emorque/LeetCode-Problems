1. List out any clarifying questions:
- Will the n ever be less than 0?

2. List out 1-3 data structures/algorithms that could be useful:
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- By drawing out some examples, there is some kind of pattern in how the output list is formed 
- With every odd number, it is always the previous number plus 1. 
- With every even number, it seems tricky
- Nevermind, so with every even number, it seems like its number of bits is just the value for itself // 2. 

4. Assess the space/time complexity:
- Space: O(n) since I need to create an output with the size n + 1
- Time: O(n) since I need to compute the value at each index, so since there are n + numbers, the time complexity is n 

5. Optional - Give any ways you would improve your solution: