1. List out any clarifying questions:
- Can I assume that the points list is not sorted?

2. List out 1-3 data structures/algorithms that could be useful:
- heap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Because I am looking for points closest to the center, I can simplify the equation to sqrt(x^2 + y^2)
- So what I am thinking, is to go through all the points, calculate the distance, and then add the distance plus the coordinates to a minheap
- Then, I'll pop from the minHeap k times and record all the coordinates that I've popped

4. Assess the space/time complexity:
- Space: O(2n) -> O(n) as I would have to have a heap of size n to records all n points and potentially a result list of size n 
- Time: O(logn * n) as the heappush/heappop is logn times which is done n times. 

5. Optional - Give any ways you would improve your solution:
- Instead of using a heap, an interesting solution I see if to use sorted with lambda 