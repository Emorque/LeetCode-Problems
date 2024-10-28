1. List out any clarifying questions:
- Does the string only contain upper case characters?
- Can there be multiple valid substrings that share the same max length?
- Can k be 0?

2. List out 1-3 data structures/algorithms that could be useful:
- Sliding Window

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I have to deal with the substrings, a sliding window approach comes to mind
- Ultimately, I have to be able to track the frequencies of the characters that I have seen. 
- That is because I need to know my frequencies so that for the current length of my substring, it can be valid by changing at most k characters
- I can do this by mainly tracking and recording the character that appears most frequently
- Once the substring is no longer valid, I'll just move the left pointer by 1 each time

4. Assess the space/time complexity:
- Space: O(n) since there is a case that the entire string is valid with unqiue characters, meaning the freq hashmap would have n keys 
- Time: O(n) since I have to process every n character at least once

5. Optional - Give any ways you would improve your solution: