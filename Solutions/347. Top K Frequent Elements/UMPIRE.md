1. List out any clarifying questions:
- Can k's value be more than the number of unique elements that I have?
- If k is 1 but I have two characters with equal top frequencies, is returning either a valid answer?

2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- When I see the word "frequent", my mind immediately turns to hashmaps as it is a very useful structure for recording frequencies 
- Then what I can is create a list of length n, as if there are n numbers, then the most frequent a number can be is n. I'll iterate through the hashmap where the key will be inserted in the list at index: value
- Then I just iterate from right to left in my list as I want the k most frequent, and populate an output list with the most frequenct characters until it has a length k

4. Assess the space/time complexity:
- Space: O(n + k + n) -> O(n). The first n comes from the hashmap as in the worst case, there can be n number of keys where n is the length of nums. k comes from the length of the output list. The second n comes from the frequency list which is n + 1 length
- Time: O(n + n + k) -> O(n). Similar reasoning as space. First n is from itearting through every number to get frequency count. Second n comes from getting all the values which at worst, could be n values. k comes from itearting through the freqlist k times

5. Optional - Give any ways you would improve your solution: