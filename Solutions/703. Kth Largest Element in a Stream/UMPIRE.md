1. List out any clarifying questions:
- Will there be any cases in which we are given less scores than our value of k? 
    - Would I then return the lowest score?

2. List out 1-3 data structures/algorithms that could be useful:
- Heap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since every time a new score gets added for me to track, I need something that can sort my structure so that I can always ontain the kth largest element
- A heap would work wonders here
- Then, I could also constrain the size of the heap to the size of k, so that I just return heap[0] each time. There's no real need for the size of the heap to be larger than k, the lower scores will not be required to find the kth largest

4. Assess the space/time complexity:
- Space: No extra space is used, as the given nums list is converted to a heap 
- Time: For the __init__ function: It will be O(n + (n-k)log(n)) -> O((n-k)log(n)). The n comes from the heapify function as heapify works inplace in linear time. The log comes from the heappop operation. The (n-k) comes from how I need to perform heappop n-k times to keep the heap at a size k
- For the add function: It will be O(2logk) -> O(logk) as I need to run heappush and heappop on the heap of size k twice 

5. Optional - Give any ways you would improve your solution: