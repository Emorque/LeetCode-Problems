1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Bitwise

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Linear runtime and constant extra space is rough
- Without these constraints, the easy solution would be to utilize a set
- Something that can do both is using bitwise logic, which does help here. 
- What we're looking for is the number in the nums list that appears once. The rest appear twice. Thinking about it another way, the numbers that appear twice cancel each other out
- Using xor can work. Since if I did 2 xor 2, then it returns 0. But if I do 2 xor 0, I get 2. And since xor is cummulative? Where order of operation doesn't matter, just doing xor on all the numbers should result in the final number being that number that appears once. The rest get cancelled out

4. Assess the space/time complexity:
- Space: O(1) since I am only using constant space
- Time: O(n) since I need to compute every num in nums

5. Optional - Give any ways you would improve your solution: