1. List out any clarifying questions:
- Can the weight of a stone be negative or 0?

2. List out 1-3 data structures/algorithms that could be useful:
- Heap

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- The biggest thing that sticks out to me is that the heaviest stones are picked and then smashed together. Then, I would have to put the remaining stone in my pile. 
- This means that I need a way to track my heaviests stones, and then need a way to maintain weight order as I put a new stone back in. 
- A heap would be a great way to do both. I'll convert the stones list into a heap, and then while the length of the heap is greater than 1, I'll take the top 2 stones, smash then, add the remaining stone back if it exists, and repeat

4. Assess the space/time complexity:
- Space: O(n) as the the moment the extra list is created to be turned into a heap, it will have a size n (n stones)
- Time: O(n + n + nlogn) -> O(logn). The two lone n's comes from the creation of the heap list and then heapify call. The nlogn comes from the while loop, as I perform heappop for every stone in the heap and then heappush a new stone, it takes log(n) to do each and since I do it n times, it results in nlogn

5. Optional - Give any ways you would improve your solution: