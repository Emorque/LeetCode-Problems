1. List out any clarifying questions:
- Do you consider using a heap as sorting?
- Are there duplicate numbers?

2. List out 1-3 data structures/algorithms that could be useful:
- Heap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Using a heap, I can heapify the nums list so that the min value is always what get popped
- Then, I can pop from nums list len(nums) -k times and return whats on top

4. Assess the space/time complexity:
- Space: O(1) since I am not creating extra space 
- Time: O((n-k)logn * logn) -> O((n-k)logn). The second logn comes from heapify. The n-klogn comes from how I need to perform logn heappop (len(nums) -k) times

5. Optional - Give any ways you would improve your solution:
- There is actually a really cool intuitive, simplier solution
- You get the minimum and maximum number in the array, Then you create a list with this range, and then go through the list again, populating the elements in it
- Then itearte backwards in this list k times until k == 0. You then return your current number