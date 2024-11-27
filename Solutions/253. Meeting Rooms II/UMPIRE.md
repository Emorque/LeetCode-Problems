1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- When thinking about intervals, it is helpful to imagine them in a kind of a timeline
- And if I were to sort these intervals by their starting times, I don't have to worry about conflicts much later down in the line 
- With that in mind, this logic works: imagine that I have in memory, some structure that will allow me to see when the soonest room is available
    - Then, I just compare that room with my current next interval, and if the current interval starts before that soonest room is open, than that current interval has to go into another room
        - Otherwise, just place this interval in the structure, while getting rid of what was previously at top
- This perfectly aligns with a minHeap, and at the end, I just return the length of the minHeap as it will contain the total number of rooms in use at the end

4. Assess the space/time complexity:
- Space: O(n) for the minHeap
- Time: O(nlogn)

5. Optional - Give any ways you would improve your solution: