1. List out any clarifying questions:
- Is the array sorted in any way? Or are anagrams placed randomly?

2. List out 1-3 data structures/algorithms that could be useful:
- Tuple
- Hashmap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- First, what determines that words are anagrams of each other, is that they share equal character frequencies
- So something I need to do, is remember the unique character frequncies that I found and then whenever I find the frequencies of my current words, I need to compare it with all the ones I've seen so far 
- So, what I think I can do, is construct a list. Usually I would use a dictionary for character frequencies, but by using the ord() function, I can use a list of 26 characters 
- Then, I can create a hashmap where the key is this list, converted to a tuple since a list can't be hashed, and the value is a list of words that are formed from the list

4. Assess the space/time complexity:
- Space: O(n * k + n). The n comes from the case where each word (n) has unique character frequencies, so there would be n keys in the dictionary. Then there is the output list where is dependent on k, which would just be the word with the largest length. The 2nd n comes from the output return, as the final list contains all n words
- Time: O(n * k + n + n) -> O(n * k). The n * k comes from the logic that for each word (n), I need to calculate each individual character (k) to create its frequency list. Second n comes from how I am looking up the dictionary with the tuple key n times. The 3rd n comes from the final return, where every word needs to be added to the list

5. Optional - Give any ways you would improve your solution: