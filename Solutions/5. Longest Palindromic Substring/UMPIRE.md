1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Instead of checking every possible substring
- Just start at the current character (or current and current + 1) and branch out on both sides
- Once a substring is no longer a palindrome, no need to continue; no amount of adding characters on both sides can make it a palindrome

4. Assess the space/time complexity:
- Space: O(1) becomes constant space is used, but if you could helper calls, it would be O(2n) for each character n
- Time: O(2n) as it is kind of like two pass 

5. Optional - Give any ways you would improve your solution: