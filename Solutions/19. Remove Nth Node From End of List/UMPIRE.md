1. List out any clarifying questions:
- Can I assume that the nth node does exist in the LL?

2. List out 1-3 data structures/algorithms that could be useful:
- Two pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- It's pretty self explanatory. Since ListNode is not a DLL, I don't have access to a prev node
- Because of that, I may need to use two pointers
- I'll have one pointer start at the head, and then the second one can move forwrad n times
- Then, I'll move both until the right pointer reaches the end. My left pointer's next node should be the nth node from the end of the LL
- Then, I just change the left pointer's next value to .next.next

4. Assess the space/time complexity:
- Space: O(1) since I am only using constant extra space
- Time: O(n) as I need to traverse through the whole LL and explore all n nodes

5. Optional - Give any ways you would improve your solution: