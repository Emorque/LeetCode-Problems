1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since this is a single LL, I can only work with .next
- I'll need to keep track of a prev and curr node, and every time, I need to remember what curr.next's node is before messing with .next values
- Then I'll set curr to that temp Node, and prev to what curr was before. 
- set prev to none, save curr.next in memory, set curr.next to prev, and set prev to curr and curr to curr.next that was in memory
- keep doing this until curr is equal to None, the tail is reached

4. Assess the space/time complexity:
- Space: O(1) since all I have created are essentially pointers in memory which take up constant space
- Time: O(n) since if there are n nodes, I need to process all n of them so that I can reverse the whole LL

5. Optional - Give any ways you would improve your solution: