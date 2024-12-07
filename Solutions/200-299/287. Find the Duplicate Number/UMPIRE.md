1. List out any clarifying questions:
- So is the duplicate number only repeated twice?
- Is there a special reason why the integers range from [1,n]?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- What is interesting is the restriction of no modifications and constant space. So this rules out using sort or a set
- The fact that the number can be repeated more that twice rules out a bitwise solution
- Even if I were to get the sum of what [1,n] would be, how can I get the duplicate if there can be multiple duplicates?
- The brute force way would be to check the entire nums list for every number to find the duplicate?
- One unique thing is that if I navigated the nums array with the numbers themselves as the next index to explore, and I use the slow, fast pointer logic like with LLs, then I can find a cycle with the repeated numbers
- The thing is that I may not always be at the repeat number with just slow, fast
- Drawing out an list as a LL and drawing the connections, I see that the entry of the cycle is the repeat number
- So just to be sure, I'll use slow,fast pointers followed by Floyd's algorithm

4. Assess the space/time complexity:
- Space: O(1) as I am using constant extra space with pointers (int variables)
- Time: O(n) since I need to iterate over all the numbers to locate the start of the cycle

5. Optional - Give any ways you would improve your solution: