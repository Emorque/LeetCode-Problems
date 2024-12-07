1. List out any clarifying questions:
- Is the array sorted?

2. List out 1-3 data structures/algorithms that could be useful:
- Sets

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Since were concerned about finding instances of when a values appears twice in the given array, one immediate thought that came to my mind was to use a set
- A set will be useful since I can quickly lookup if any value is in a given set with "in"
- I'll initialize a set, and then while iterating through the array, add values to the set if it is not in it, and return True if it is 
- If I manage to traverse through the whole array without returning True, then I return False. The array only has distinct elements

4. Assess the space/time complexity:
- Space: O(n), and it is from the set. In the case were every element in the array is distinct, then the size of the set grows to be exactly the same length as the array. 
- Time: O(n), since I would have to traverse through the entire array. Maybe all elements are distinct or there is a duplicate in the last two indexes, I can't end the traversal early

5. Optional - Give any ways you would improve your solution:
- This is less of an optimization, but more so a what if
- If the array was sorted, then I could just check if my current num and the one next to it are equal. This would save the need of an additional data strucutre, because in an unsorted array, duplicate nums could be anywhere in the array