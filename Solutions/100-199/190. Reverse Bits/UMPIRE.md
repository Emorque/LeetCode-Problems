1. List out any clarifying questions:
- Am I returning the reversed number as its bit representation or as an integer?

2. List out 1-3 data structures/algorithms that could be useful:
- Bitwise

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So, given an int that represents a 32 bit unsigned integer, I need to return the integer that is represented by the reverse of this 32 bit unsigned integer
- So, what I can do is take n and use "& 1" to determine what the rightmost bit is. I can then take that bit and add it to my answer int that I am building. Then I use << and >> to shift both numbers

4. Assess the space/time complexity:
- Space: O(1) as I am only using constant space variables 
- Time: O(32) as I need to compute all 32 bits in the given n number, so 32 iterations

5. Optional - Give any ways you would improve your solution: