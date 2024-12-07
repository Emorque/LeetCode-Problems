1. List out any clarifying questions:
- Any chance the nums list is sorted?

2. List out 1-3 data structures/algorithms that could be useful:
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- One brute force one I can think of, is taking the nums list and converting it to a set. Then, going from 0 to n, I can do someting like (i in nums) to see if a number is in the set. Lookup will be O(n) for checking all n numbers (O(1) individually) but the conversion will be O(n). The number that is not in nums is the missing number
- If I want to be a bit more efficient, something I can do to remove the need of extra data space, is to use bitwise
- I know that xor is a great way of determing what number appears twice in a list. If I use xor on the same number, the result is 0. But if I use xor on two different numbers, the result is non-zero. 
- Since I know that answer should be within the range of [0,n], just that it is missing from the list, I can iterate through the list, and then use xor in the current num and use an iterator i
- There should only be one number in the iterator that is not in num, and in the end, it should be what is left 

4. Assess the space/time complexity:
- Space: O(1) since I am just using constant space variables
- Time: O(n) as, for every number in nums, I need to process it

5. Optional - Give any ways you would improve your solution: