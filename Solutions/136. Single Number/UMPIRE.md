1. Share questions you would ask to help understand the question:
- What is the range that each element can be?
- Can we have a test case of just one element? Would you just return that one?
- So every element can appear only once or twice? No thrice?
- Is the array sorted?
- What is the range of the length of nums?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Brute Force (Unlikely)

3. Write out in plain English what you want to do: 
- The first brute force solution that came to my head, was, for each num, traverse to the right of the list, and the moment that a duplicate is found, move onto the next and store that number somewhere so it is skipped later. 
    - If the end of the list is reached, then that num is the number that only appears once
- The problem with this solution is that it would be n^2 time, and would need something like a set (O(n)) to store already processed numbers
- From here, I could either use a solution that has a set that gets the element frequency. Adding when the number is not in the set, and removing if it is. At the end of the traversal, return the lone element from the set
    - This is better for time O(n), but has O(n) space
- I could also sort at the start, and then just check pairs of elements, if there is no matching, than one of those elements is the answer
    - This has constant space, but O(nlogn) for sorting
- Neither are can do both, so how can a solution be optimized to be done in linear time and with constant space?
- The answer is to used xor. Bascically, by using xor, I can compare two elements togehter.
    - And another great thing about xor, is that it doesn't care about the order of the expression, like an expression of only multipliying/adding
    - With xor, the numbers are converted to their bit representations 

4. Translate each sub-problem into pseudocode:
- Set an initial number to 0, because every number that is xor'd with 0, just returns itself. And even if we have a test case of a single element 0, 0 would be returned 
- Then, for every num in nums:
    - set output to output ^ num (^ is xor) in python

- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0

        for num in nums:
            output = output ^ num
        
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the solution is done in linear time and with constant extra space
- One weak area is that this solution is only intutive if someone is familiar with how xor works. Had I gone through an example, the reasoning behind why xor works becomes clear