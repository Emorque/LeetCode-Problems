1. List out any clarifying questions:
- When provided with a number from addNum, are they always in increasing order?

2. List out 1-3 data structures/algorithms that could be useful:
- Heap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since I need to make sure that the integers added with addNum are mantained in an ordered list, the brute force approach would be to use a sorting algorithm each time addNum is used on a list
- Instead, something else I can I do is main this structure with a heap. Then, by the length of the heap, I can determine how many numbers I need to pop before I can start calculating the median.
- Finally, I store all the popped values in some other strucutre and then readd them to the heap once the median is calculated

- This is a an okay solution but not the best complexity wise
- Instead of constantly destroying and repairing a heap, two heaps can be used

- As long as I can have two heaps represent both halves of the stream, then obtaining the medium is easy computationally. 
- The trick comes in how these heaps are populated
- To do so, I can just use the 0th index of each heap to determine where each new num should be placed
- Then, it comes down to maintaining that the lengths of each half are relatively equal. 
- findMedian then becomes just looking at each half if length or odd or both if even

4. Assess the space/time complexity:
- Space: O(n) for all the added numbers
- Time: O(1) for findMedian. O(logn) for addNum with at most 3 logn heap operations for each addNum call

5. Optional - Give any ways you would improve your solution: