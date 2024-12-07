1. List out any clarifying questions:
- Can the given string be of length 1?

2. List out 1-3 data structures/algorithms that could be useful:
- Two Pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- One way to go about the solution is to see if the reverse of the given string is equal to the given string
- I think a more efficient solution would to, instead try with two pointers. 
- I'll have one on each end, and if the letters match, then the read characters so far represent a valid palindrome 
- I'll keep this this until the two pointers intersect, if they do, that means all corresponding characters match, so it has to be a palindrome

4. Assess the space/time complexity:
- Space: O(1), since I am using a two pointer approach which take up constant space, it results in O(1)
- Time: O(n), since I need to process each individual character in the given string. So if there are n characters, I need to process all n characters in True test cases. 

5. Optional - Give any ways you would improve your solution:
- If I were not allowed to utilize isalnum() or lower(), I would create two seperate helper functions that would use the ord function to check if the given character is alpha-numeric and set the character to lowercase respectively. 