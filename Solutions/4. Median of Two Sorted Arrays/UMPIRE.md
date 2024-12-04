1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Binary Search

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The brute force approach is to just take the two sorted arrays and merge them into one sorted array
- Then, I just return the median of this newly created sorted array
- This leads to O(m+n), but the constraint of log(m+n) for LC makes this a difficult problem

- The key logic is to think of this problem as starting with two separate arrays, and then breaking them into 2 halves, 2 halves that should be equal to the length of both these arrays added together divided by 2. 
- Until I am able to makes two successful halves that effectively match what the merged array would look like, I just need to continue performing binary search 

4. Assess the space/time complexity:
- Space: O(1)
- Time: O(log(n + m))

5. Optional - Give any ways you would improve your solution:
- This is a very difficult problem, but at the very least being able to initute the logic of these two halves does get me half of the there. It will continue to be learning process until I am comfortable solving this in 45 mins or less. 