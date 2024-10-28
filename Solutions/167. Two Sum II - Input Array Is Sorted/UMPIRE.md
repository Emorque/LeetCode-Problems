1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- 2 pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- There are actually two things that are pretty key to note
    - The array is sorted in ascending order
    - The solution I provide has to use extra constant space
- The brute force way, is to start from each number, and then check every possible pairing to see if they can sum to target
    - If I get a pairing whose sum is greater than target, I can just stopping seaching with the starting number, since numbers further to the right are greater
- With that kind of logic, I don't need to check every possible pair
- What I can do is instead have the greatest possible sum from a pair and then slowly decrease the sum untill I reach the target
- Since the array is sorted, I can always get the greatest possible sum by using the first and last number
- Maybe greatest isn't the right word, I would say the one that can most easily grow or shrink
- If I need to grow my sum, I can just move my left number by 1
- If I need to decrease my sum, I can just move my right number by 1

4. Assess the space/time complexity:
- Space: O(1), since I am only using int variables as pointers of the numbers list
- Time: O(n), since in the worst case scenerio where the two numbers I need are directly in the middle, I would have to process all n numbers

5. Optional - Give any ways you would improve your solution: