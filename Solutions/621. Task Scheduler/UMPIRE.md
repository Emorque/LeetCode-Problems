1. List out any clarifying questions:
- Are the tasks sorted in any way?
- Can n be 0?

2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap
- Heap
- Queue

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- I think it would be useful to know the frequencies of these tasks, since they aren't sorted
- With the frequencies, I can then put them in a heap 
- The next step comes from poping from this heap and placing those tasks somewhere else in memory, keeping in mind to decrement its frequency and marking at what time I can use it again

4. Assess the space/time complexity:
- Space: O(n + n) -> O(n), the first n is for the hashmap if there are n keys for all n tasks. The second n is kind of a mixture of the heap and queue, since in the worst case scenerio, they will both hold a maximum of n tasks
- Time: O(n + nlogn + logn*n). The first n is for gathering the frequencies. The second and third nlogn have to do with the number of heappushs/heappops that are happening which at worse could be n times logn

5. Optional - Give any ways you would improve your solution:
- Lot of more optimal solutions that I will definetly relook at 