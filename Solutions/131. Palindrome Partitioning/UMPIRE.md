1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Backtracking

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- It would be very helpful to have an outside isPalindrome function, since that is what I will be splicing my string by
- I'll have a helper function to preform backtracking, since I want to create as many possible palindromes with the current character before moving onto another set of partitions
- helper with use an index and the base case will be when that index reaches the end of s
- I'll call isPalindrome on my current string
- If it is valid, then I'll append it to my palindrome list and move onto the next index with a blank slate 
- evantually, it should backtrack back to the original character
- Instead of indexes, I can rework this to work with substrings by cutting the cutting where a palindrome is found

4. Assess the space/time complexity:
- Space: O(n * m) for the number of partitions made n and m for the average length of each partition 
- Time: O(2^n) in the case that I make the choice to partition the substring n times and then carry on

5. Optional - Give any ways you would improve your solution: