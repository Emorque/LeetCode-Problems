1. List out any clarifying questions:
- Does order matter? So are [-1,1,0] and [0,1,-1] considered duplicates?

2. List out 1-3 data structures/algorithms that could be useful:
- Two pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- So I can't have any duplicate triplets
- The brute force method would be to check every possible triplet, and even once one is found, I would have to compare it with every found triplet so far so that no duplicates are recorded
- Honestly, I think having the list being sorted makes this much simplier. That way, I can just iterate over every number, and then in for each number, I'll perform a two pointer with the rest of the list to see if I can find a pair that sums to (-)number.
- And to take care of any duplicates, if I find a duplicate as a neighbor, then I can just skip it
- I couldn't do that with a nonsorted array since duplicate numbers couldve been anywhere. In a sorted array, they're next to each other

4. Assess the space/time complexity:
- Space: O(n) as the length of the list I end up returning is dependent on the length of n 
- Time: O(n^2 + nlogn) -> O(n^2). The nlogn comes from the initial sorting of the list. The n^2 comes form the fact that I need to process n - 2 numbers, and then for each, I will in the worst case scenerio, have to look at all n numbers in the rest of the list

5. Optional - Give any ways you would improve your solution: