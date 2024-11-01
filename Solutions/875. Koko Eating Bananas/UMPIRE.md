1. List out any clarifying questions:
- Will h always be greater than my length of piles?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- After thinking about what if koko ate a billion bananas, the most amount of bananas that Koko would eat for her to finish every  pile in an hour would be max(piles)
- So my ideal k would be in the range of [1, max(piles)]
- the brute force way would be to check from the range from left to right, and return the first k that results in a time that is <=h. Any more and it is no longer than minimum I need
- however, this would be n^2 since I'd check the entire piles list n times if k is near the end of the range
- I can change this to nlogn by performing binary search. The closer a k is to 1, the longer it takes to eat the bananas. Wherea the closer k is to max, the quicker it takes

4. Assess the space/time complexity:
- Space: O(1) since I am using constant extra space
- Time: O(n + logm). The first n comes from getting max at the start. The logm where m represents the highest value in the piles, is the binary search logic. Work gets halved every iteration

5. Optional - Give any ways you would improve your solution:
- My while loop does work, but there is a more efficient simpier approach by using ciel and getting: "time += ceil(pile/mid)"