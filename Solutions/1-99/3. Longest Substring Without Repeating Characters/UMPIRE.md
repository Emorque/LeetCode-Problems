1. List out any clarifying questions:
- Are characters that are the same but different casing considered repeating?

2. List out 1-3 data structures/algorithms that could be useful:
- Sliding window

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The brute force approach would be to check every single substring
- However, there is a simplier approach that is more time efficient. 
- If I just iterate from left to right, keeping track of the characters I've seen in a set, I can easily detect whenever I come accross a duplicate
- Then, I can just move my left pointer till I remove the duplicate
- Every time this happens, I'll be sure to record the max length

4. Assess the space/time complexity:
- Space: O(n) since there could be case where the entire string doesn't have duplicates, so the seen set would contain all n characters
- Time: O(n) since I have to process and check every character in the string 

5. Optional - Give any ways you would improve your solution: