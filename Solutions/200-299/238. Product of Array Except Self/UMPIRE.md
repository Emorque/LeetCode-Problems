1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DP?

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The constriction of not using division does make the easiest solution in mhy head not viable
    - I would just get the product of the whole array, keeping track of any zeros and then rerun through the list, and dividing the current number from the product

- Prefix and suffix makes me think of all previous numbers, and all next numbers
- I need a way to track all previous numbers upto my current number, and all next numbers
- I don't think it's possible on one pass, I may need to do two seperate passes for prefix and then suffix
- So, I can make a list that hold all my prefix values for the corresponding number, and then multiply those by the suffix values 
- Prefix will be from left -> right, and suffix from right -> left. So multiplifying the two would be the product of the current number except self

4. Assess the space/time complexity:
- Space: O(n) as it is a new list that I am returning with size n (same number of elements in given nums list)
- Time: O(2n) -> O(n) as I need to perform two complete passes from the nums list, which is of size n

5. Optional - Give any ways you would improve your solution: