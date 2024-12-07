1. List out any clarifying questions:
- Can k be 0 or 1?

2. List out 1-3 data structures/algorithms that could be useful:
- Heap
- Two Pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- By running through an example, there are two approaches that I saw
- One is to iterate through every list and, in a vaccum, perform mergeList between it and my current result LL. Then, do the same for the next list
- Second, is to iterate through each head in the given list and push them to the minHeap. Now, just pop the value from whichever value is smallest, and if the popped node still has nodes after it, push it back to the minHeap
    - Since the original node doesn't have an __it__ to compare in heap, I need to create a class to does

4. Assess the space/time complexity:
- Space: O(k), where k is the number of lists, as thats the maximum number of nodes in the heap at once 
- Time: O(nlog(k)), where k is the number of lists and n is the total number of nodes across all LLs. Since the heap is at most size k, that goes in log, I perform heap operations n times

5. Optional - Give any ways you would improve your solution: