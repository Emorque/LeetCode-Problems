1. List out any clarifying questions:
- What kinds of characters are s1 and s2 comprised of?

2. List out 1-3 data structures/algorithms that could be useful:
- Sliding Window
- Hashmap 

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I am going to have to see if a permutation can be arranged in s2, sliding window seems like a clear fit. That way, I can grow my permutation one character at a time, and if there is a case in which my built permutation no longer is valid, I can shift the left pointer until it is
- The first step would be to get the character frequency of s1. Order doesn't matter, so long as a permutation can be built with every character in s1
- Then I'll iterate through the s2 string
- If I don't find a character in s1, I'll continue 
- Once I do, then one of two things happens
    - My current character is still valid
    - My current character is invalid. I have begun to build a permutation but my current character makes the permutation unable to be completed. Either I overextend by adding one more character or I come across a character that is not in s1 at all
- I'll only return True if the difference between my two pointer is equal to the length of s1. If it is, then I'll know I've built the permutation
- If I never return True in the loop, I return False out of it

4. Assess the space/time complexity:
- Space: O(n) where the n represents the number of characters in s1. If every character in s1 is unique, then the hashmap would have n keys
- Time: O(m) where m represents the number of characters in s2, since all m characters have to be checked

5. Optional - Give any ways you would improve your solution: