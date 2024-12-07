1. List out any clarifying questions:
- So you say "not to use the same element twice", but does that mean I can use the same number twice, if it appears twice?
- Is the array sorted?

2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- One brute force way to go about this problem, would be to iterate through the entire nums list for every num, to see if there are any pairs that equal target
- Since the end goal is to see if I can find a matching difference for each num, what I can do is keep a record of differences that I need with a set and then know that a pair is found when I find that difference in the future
- Since I do need the indexes, I'll use a hashmap instead of a set, with the difference as the key, and the index as the value

4. Assess the space/time complexity:
- Space: O(n) since the extra hashmap has keys that grows in relation to the number of unique numbers in the nums list. If one unique number is added, that is one extra key 
- Time: O(n) since I need to at worst, traverse through all numbers in nums to find a pair. When it comes to looking up and setting keys/values in the hashmap, that is all O(1)

5. Optional - Give any ways you would improve your solution: