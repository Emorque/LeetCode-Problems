1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- Decision Tree + Caching
- DP

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Overall, in a brute force solution, this looks like it can be solved with a helper function with decision tree logic
- That was what I had originally, and the problem was that the time complexity was coins^amount, as we could make len(coins) number of decisions and the height of the decision tree was from 0 to amount, i.e. amount
- However, with caching, this can be improved to coins * amount, since that is the number of unique keys in the hashmap
- Only two lines where changed, as I don't have to use this for loop, I can just set my current key equal to the two scnerios that build up to it, either adding the current coin or not and moving onto the next. The sum of these two scenerios is the resulting number of combinations
- I then set the value in the cache and return res

4. Assess the space/time complexity:
- Space: O(len(coins) * amount)
- Time: O(len(coins) * amount)

5. Optional - Give any ways you would improve your solution:
- This can be taken a step further to use a 2d matrix for a dp solution, which can then be simply the space to amount, as I don't need to continue previous coins. 
- Remember that I can do from decision tree -> decision tree with caching -> dp -> optimized dp