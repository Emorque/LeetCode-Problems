1. List out any clarifying questions:


2. List out 1-3 data structures/algorithms that could be useful:
- DP 
- Decision Tree + caching

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- This looks like a decision tree problem, where there are two decisions at times where the indexes of s1 and s2 match the index at s3. If that is the case, the decision tree diverges
- Otherwise, if just becomes a matter of checking if one path can cleanly make it to the end
    - The end is when the indexes of both s1 and s2 equal to the length of s3, meaning that all the characters from s1 and s2 have built s3
- Ultimately, I return True if I can sucessful return a true back up to index 0, 0
- This is a 2^m + n solution, which can be optimized to m *n with caching (b/c there are only m *n keys in the cache). (m and n are the lengths of s1 and s2 respectively)

4. Assess the space/time complexity:
- Space: O(m * n)
- Time: O(m * n)

5. Optional - Give any ways you would improve your solution:
- As with many decision tree problems, they can continually be optimized until you set the space complexity to as small as it can be. In this case, it would be the length of the smaller string (s1 or s2)