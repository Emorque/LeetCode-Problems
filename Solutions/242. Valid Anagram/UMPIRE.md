1. List out any clarifying questions:
- Are the two strings guarenteed to be the same length?

2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So what determines if two strings are anagrams of each other, is if they share equal character frequencies
    - if they share the same characters, each of which appear at the same number of times, then they are anagrams
- A hashmap would work great here
- I'll interate through both strings, keeping character frequency in a hashmap
- Actually, I can just have one hashmap for string s, then when iterating through string t, if a character is in the hashmap, then decrement the value by 1, but if that value is 0, then t and s share the same character, but it appears in t more times
    - And if the character is not in the hashmap, then return False, since there is a character is t not in s, so they can't be anagrams
- This lookup should be fast since hashing is utilized O(1) lookup
- Return True if all the values in the hashmap are 0, or actually just return True at the end if they are of equal length

4. Assess the space/time complexity:
- Space: O(n), this is the frequency hashmap that could have n keys (n is the length of s) if ever character is unique
- Time: O(1 + 1 + n + n) -> O(2n) -> O(n). This 1s come from the len() function, since in the python, this function is run in constant time. The ns comes from the fact, after len() is used and the lengths of both strings are equal, I need to traverse through all characters in both strings, so 2n where n is the number of characters

5. Optional - Give any ways you would improve your solution:
- If I really wanted to use python optimizations, I could have used the collections library and just compared the Counter() of each string. Counter(s) would return a counter object that contains the character frequencies of s. 