1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Bitwise

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I am looking for the number of 1s bits in the n number, I need to way to get each bit in n to evaluate
- Using & should help in determining if the right most bit is 1. If n & 1 results in 1, that means that the rightmost bit is a 1, else it'll result in 0. Then, the compute the next right most bit, I can just shift n with >> 1.
- I'll do this until n == 0

4. Assess the space/time complexity:
- Space: O(1) since I the only extra space is constant
- Time: O(d) where d represents the number of bits n has, as they all have to be computed

5. Optional - Give any ways you would improve your solution: