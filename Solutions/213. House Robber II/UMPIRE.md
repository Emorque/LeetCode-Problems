1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Keep the logic of House Robber 1, but put it in a helper function
- Then, call that helper function with different ranges to represent two journeys where I can only rob the first or last houses

4. Assess the space/time complexity:
- Space: O(1) since I am only using constant variabales and I only ever call helper twice for all test cases
- Time: O(2n) -> o(n) for the 2 passes I make on nums

5. Optional - Give any ways you would improve your solution: