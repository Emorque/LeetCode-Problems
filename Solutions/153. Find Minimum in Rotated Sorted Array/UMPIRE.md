1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Binary Search

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So given an array that starts out sorted in ascending order, the given array is that array but rotated 1-n times. Any more than n, and it would be the same as 2 (n + 2 rotations = 2 rotations)
- Goal is to find min and I need logn time which screams binary search
- So the array is still sorted, but the order may be misaligned.
- An edited form of binary search is needed
- If mid is less than high, then min should be between low and mid
- else, min should be between mid + 1 and high

4. Assess the space/time complexity:
- Space: O(1) since I am just using constant extra space
- Time: O(logn) since I am halving my work each iteration with binary search

5. Optional - Give any ways you would improve your solution: