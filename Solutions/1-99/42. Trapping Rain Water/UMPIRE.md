1. List out any clarifying questions:
- Are there sides at the ends of the list?

2. List out 1-3 data structures/algorithms that could be useful:
- Sliding Windows / 2 Pointer

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- Just going from left to right, it looks like I just need to be concerned about how much water I can contain until I find a height greater than my current height
- Until that point, I can just add any differences in heights to some current sum variable
- Then, once I find a height that is >= my starting height, I can consider the container complete, and add it to my cummulative sum 
- By thinking of more and more edge cases, the less correct this solution appears to be. If I were to go down this route, I would end up adding multiple if and while conditions, complicating the code and making it harder and harder to follow. 

- Rethinking about the problem, the logic can be made simplier if I think about each height in its own container of length 1. For a height of h, the most amount of water that can be contained at this index is the minimum of (the max height to its left, the max height to its right) minus whatever its current height is * 1. 
- To break this down: "minimum of (the max height to its left, the max height to its right)":
    - The max height of left and right are needed to determine how the biggest possible container it can be apart of
    - The min is needed, as the container is constrained by the smaller height, as water cannot be curved, it is flat. 

4. Assess the space/time complexity:
- Space: O(n)
- Time: O(n)

5. Optional - Give any ways you would improve your solution: