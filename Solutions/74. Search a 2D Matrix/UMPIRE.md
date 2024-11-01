1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Binary Search

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This looks like a binary search problem. The matrix being sorted as such really hints at this
- Since that is the case, I think the more optimal way to perform binary search, would be to pinpoint the exact middle position of the matrix at each iteration. However, that is a bit complex right now, so I think a simplier approach would be to perform binary search to find a viable row, and then perform binary search on that row if found
- If a valid row is not found or the number is not found in the valid row, return False

4. Assess the space/time complexity:
- Space: O(1) since I am only using int variables are pointers in binary search 
- Time: O(logm + logn) -> O(log(m * n)), since this algorithm performs binary search on m rows and then binary search within on n columns

5. Optional - Give any ways you would improve your solution: