1. List out any clarifying questions:
- Are there duplicate numbers in the list?

2. List out 1-3 data structures/algorithms that could be useful:
- Set

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- With O(n) time being a requirement, that basically means that I have to come up with a solution that only performs one pass of the array. Any kind of sorting is O(nlogn) time
- To detemine that a sequnce is consecutive, the numbers in it have to be directly after one another, so something like "1,2,3" works but not "1,3,4"
- So in that case, we only points that matter are the starting and ending points
- What I can do then, is run through the list, and to determine if I am at a starting point, I'll check if my current number - 1 is in the list. If it is, continue, but if it isn't then I am at a starting point, and I keep count of all numbers that are in this sequence
- The thing is that checking n-1 for each number would be time intensively as I'd have to lookup the entire list in a worse-case scnerio. 
- The solution to this would be to convert the list to a set which would would just one instance of O(n) with O(1) lookups, as oppsoed to no conversion and n O(n) lookups 

4. Assess the space/time complexity:
- Space: O(n) since I need to create a set with at worst, n numbers
- Time: O(2n) -> O(n) since in the worst case scnerio, I need to process all n numbers in my loop. Then the other n comes from converting my list to a set

5. Optional - Give any ways you would improve your solution:
- While the solution works, there is actually a solution with union find that I will check out. The logic seems similar to the idea I had with finding starting points, so I'll dive deeply on why and how it works exactly