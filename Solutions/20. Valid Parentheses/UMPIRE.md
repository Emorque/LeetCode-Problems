1. List out any clarifying questions:
- So if the first character in the string is a closing bracket, I should immediately return False, correct?

2. List out 1-3 data structures/algorithms that could be useful:
- Stack

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- A stack would work great here, as I can kind of build up a solution using that first-in-last-out logic
- So by appending values to my stack, I can keep in memory previous opening brackts, to then check if the next closing bracket matches the next opening one
- So, now it comes down to keeping track of each possible scnerio and having them be conditionals

4. Assess the space/time complexity:
- Space: O(n), since the size of my stack grows in relation to the number of characters in the s. If, for example, there is a test case of only n opening brackets, then the stack will be of size n at the end
- Time: O(n), since I need to process every character in the string for some test cases. When it comes to appending and popping from my stack, that is all in constant time O(1)

5. Optional - Give any ways you would improve your solution:
- This solution does a good job, but there is some repeat logic, between the last 3 elif statements. One way to make the code cleaner would be to have the relationships between the opening and closing brackets be represented elsewhere, in something like a hashmap. Then, I would only need to query that structure and use the same logic I used here once in the loop.