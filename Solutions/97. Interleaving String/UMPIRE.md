1. Share questions you would ask to help understand the question:
- The substrings have to be interleaved consecutively correct?
  - I cannot interleaving a substring from the end of s1 if I still have substrings before it?
- Can s1 and s2 be vastly different lengths?
- What kinds of characters are in the strings?
- What is the range I can expect for the lengths of the strings?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP (Likely)
- DFS (Neutral)

3. Write out in plain English what you want to do: 
- By drawing with decision tree with with maintaining the value (index of S1, index of s2), I was able to come up with a dfs solution that will eventually lead to the end of s3 as it is traversed.
  - If the end of s3 is reached, then True is returned and that True then travels back up to the top where it is returned
    - With this recursive dfs approach, I can optimize it further by using a cache to store the boolean values of (index of s1, index of s2) if it's path leads to a True or False
      - That way this can be referened later, saving some time

4. Translate each sub-problem into pseudocode:
- 3 talks about dfs with caching
- Now, this is how the solution can be done with a 2d dp approach:

- Going from right to left, bottom to top of the grid, I can check whether the current indexs of s1 and s2 (bascially the coordinates in the 2d array), can they create the substring in s3 at [s1 + s2]
- If so, set the current cell to True
- However, if both indexes are equal to the current index in s3, then the diverging from the dfs approach applies here:
  - check the bottom neighbor and right neighbor to see if there are paths where using either character leads to a True
    - Pretty much this: hashmap[(s1Index, s2Index)] = dfs(s1Index + 1, s2Index) or dfs(s1Index, s2Index + 1)
      - In this case, instead of checking or, we check the already computed right and bottom neighborings

5. Translate the pseudocode into Python and share your final answer:
  <!-- if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                # every cell is already False so if neither if statements execute, cell can be left alone
        return dp[0][0] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this solution uses the logic from the dfs approach, and instead of a recursive stack, a static grid is used in reference 
  - Becomes a LOT MORE space efficient, even if still the same time efficiency
- One weak area is that this solution can in fact still be optimized. A 2d dp approach can lead to a 1d array with 2 arrays, since after some time in a 2d array, past rows are no longer needs and can be considered "unused memory"

- *I included my first dfs with cache solution in the py file