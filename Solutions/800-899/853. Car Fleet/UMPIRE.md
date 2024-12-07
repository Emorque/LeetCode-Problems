1. List out any clarifying questions:
- Is any array sorted?
- Will a car's position ever be past the target?
- If cars meet at the target at the same time, are they the same fleet?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since the arrays aren't sorted, determining the fleet that a car ends up in ends up being to compare its time to arrive to every single other car's time to arrive (to the target). 
- Even if I do have a car that my current car would end up joining, there could be a car much farther down the list that my current car would join sooner
- If I sort the cars by position closest to the target, and then calculat their TOA (time of arrival), I can determine the fleets. Going from closest car to farthest, if I come across a car that has a greater TOA than the previous, it is a part of a new fleet, as it would never catch up to the one with a lower TOA (because it would get to the target sooner)
- So I can have two ints, one that tracks the number of fleets, and one that tracks the current greatest TOA.
- The big conditional is if currentTOA > maxTOA as when this happens, I am now looking at a new fleet. If it isn't true, then I am looking a car that is joining an existing fleet

4. Assess the space/time complexity:
- Space: O(n) as I create a new track list that holds the n positions and speeds
- Time: O(n + logn + n) -> O(n). First n is creating the track list. logn comes from sorting. Third n comes from iterating backwards from the track list to do the fleet logic 

5. Optional - Give any ways you would improve your solution: